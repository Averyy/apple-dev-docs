# ReservedRegion

**Framework**: SwiftUI  
**Kind**: struct  
**Role**: Structure

A region within a view’s coordinate space that another entity reserves.

**Availability**:
- iOS 27.1+
- iPadOS 27.1+
- Mac Catalyst 27.1+
- macOS 27.1+
- tvOS 27.1+
- visionOS 27.1+
- watchOS 27.1+

## Declaration

```swift
struct ReservedRegion
```

## Overview

A reserved region indicates an area within a view’s coordinate space that an entity, such as the device hardware, reserves. Arrange the view’s content to account for this region. Each region describes a frame, margins, active state, and an identifier. For example, a camera or the Dynamic Island can cover part of the display, and the hinge of iPhone Duo divides the display into two halves.

There are two categories of reserved regions, which you specify with a [`ReservedRegion.Kind`](./reservedregion/kind-swift.struct.md) value:

- [`occlusion`](./reservedregion/kind-swift.struct/occlusion.md): An area where an element, such as the Dynamic Island, a camera, or window controls, covers content. Place content outside this area.
- [`division`](./reservedregion/kind-swift.struct/division.md): An area where content splits into separate regions, such as at the fold of a hinge. Arrange your content into separate sections on each side of this area.

## Get the reserved regions that intersect your view

Parts of the display aren’t available for your content. For example, a camera or the Dynamic Island covers part of your view, and the fold of iPhone Duo splits it in two. The system describes each of these areas as a reserved region.

Framework-provided views, such as split views and sheets, adjust for reserved regions for you. If you build a custom view that places its own content, find out where the reserved regions are and arrange your content around them.

To get the reserved regions, wrap your content in a [`GeometryReader`](./geometryreader.md), which gives you a [`GeometryProxy`](./geometryproxy.md). Then call [`reservedRegions(kind:options:layoutDirectionBehavior:)`](./geometryproxy/reservedregions%28kind,options,layoutdirectionbehavior%29.md) on the proxy. Use the `kind` parameter to choose which regions you want: `.occlusion` for areas that cover your content, such as a camera, and `.division` for areas that split it, such as the fold. By default, the method returns only active regions that currently affect your view. The following example shows how many regions cover part of the view:

```swift
struct RegionReader: View {
    var body: some View {
        GeometryReader { proxy in
            let regions = proxy.reservedRegions(kind: .occlusion)
            Text("Occlusion regions: \(regions.count)")
        }
    }
}
```

The method returns only the regions that overlap your view, including a partial overlap. For example, if a camera region overlaps with a corner of your view, its frame can start at negative coordinates or extend past the view’s size. Regions elsewhere on the screen don’t appear in the results.

Each region has a [`frame`](./reservedregion/frame.md), a rectangle that describes where the region is within your view. The frame uses your view’s own coordinates, not the screen’s: `(0, 0)` is the view’s top-leading corner, and the values are in points. The frame already includes the region’s [`margins`](./reservedregion/margins.md), which is extra space around the reserved area that keeps interactive content clear of it, so you don’t need to add the margins yourself.

## Keep content visible around occlusion regions

An occlusion region covers part of your view; people can’t see content that you place there. Use the [`frame`](./reservedregion/frame.md) of each occlusion region to move your content out of the way by changing its position, padding, or spacing.

The following example keeps a control bar, a custom row of buttons along the top of the view, clear of a region at the top. It checks only the regions that overlap the area the bar reserves, because an occlusion region can be anywhere in the view. It then pads the bar down, below the lowest of those regions:

```swift
struct TopControls: View {
    private let barHeight: CGFloat = 60

    var body: some View {
        GeometryReader { proxy in
            let regions = proxy.reservedRegions(kind: .occlusion)
            let barFrame = CGRect(
                x: 0, y: 0, width: proxy.size.width, height: barHeight)
            let topInset = regions
                .filter { $0.frame.intersects(barFrame) }
                .map(\.frame.maxY)
                .max() ?? 0

            ControlBar()
                .frame(height: barHeight)
                .padding(.top, topInset)
                .frame(maxHeight: .infinity, alignment: .top)
        }
    }
}
```

When you arrange many views, move that work into a custom [`Layout`](./layout.md). In the following example, `RegionAvoidingLayout` is a layout that you write yourself. It takes the reserved regions from the geometry proxy, and places each view it contains in a spot that doesn’t overlap a region:

```swift
GeometryReader { proxy in
    RegionAvoidingLayout(
        regions: proxy.reservedRegions(kind: .occlusion)
    ) {
        ForEach(items) { item in
            ItemView(item)
        }
    }
}
```

Make sure a region’s frame and your layout’s positions use the same coordinates. The frame is measured from the top-leading corner of the view you read it from, but the `bounds` that a layout receives in [`placeSubviews(in:proposal:subviews:cache:)`](./layout/placesubviews%28in,proposal,subviews,cache%29.md) don’t always start at `(0, 0)`. Do your calculations from `(0, 0)`, and add `bounds.origin` only when you place each view.

## Split your content at a division

A *division region* is an area that splits your view into separate parts, such as the fold of iPhone Duo. A division is active only when the device is partially open or closed. When iPhone Duo is fully open, the division is inactive, so [`reservedRegions(kind:options:layoutDirectionBehavior:)`](./geometryproxy/reservedregions%28kind,options,layoutdirectionbehavior%29.md) returns no division regions.

When a division is active, content that crosses it is hard to read and use, so keep each view entirely on one side of the division. Because a division can run in either direction, the sides depend on how someone folds the device. When you partially fold iPhone Duo like a book, the fold runs vertically at the center of the display, so your content sits side by side. When you partially fold it like a laptop, the fold runs horizontally across the center of the display, so your content stacks above and below the fold.

The following example splits a view into two panes around a division. It compares the width and height of the division’s frame to find which direction the fold runs, then sizes each pane to fit on its respective side. The clear space between the panes is the size of the division, which keeps your content out of it. When there’s no active division, the example shows a single pane. The example uses the first division, because iPhone Duo has one fold. `FirstPane` and `SecondPane` are views that you define:

```swift
struct SplitContent: View {
    var body: some View {
        GeometryReader { proxy in
            if let division = proxy.reservedRegions(kind: .division).first {
                let frame = division.frame
                if frame.height > frame.width {
                    // The division runs vertically, so split side by side.
                    HStack(spacing: 0) {
                        FirstPane()
                            .frame(width: frame.minX)
                        Color.clear
                            .frame(width: frame.width)
                        SecondPane()
                            .frame(width: proxy.size.width - frame.maxX)
                    }
                } else {
                    // The division runs horizontally, so stack the panes.
                    VStack(spacing: 0) {
                        FirstPane()
                            .frame(height: frame.minY)
                        Color.clear
                            .frame(height: frame.height)
                        SecondPane()
                            .frame(height: proxy.size.height - frame.maxY)
                    }
                }
            } else {
                // Lay out your content as a single region.
                FirstPane()
            }
        }
    }
}
```

As someone folds and unfolds the device, your layout changes with the division. When you adjust your layout for the fold, move only what’s necessary to keep elements visible and easy to tap. Controls that disappear or shift dramatically are harder to find and track, so favor small adjustments over rearrangement. If your layout is a grid, use an even number of columns so your content divides cleanly at the fold.

If your content is two related views that sit side by side or one above the other, use [`ArrangementView`](./arrangementview.md) instead of reading the division yourself. For more information, see “Choose where to check for regions,” below.

## Choose where to check for regions

Most apps don’t need to check for reserved regions. Framework-provided views, such as split views, tab bars, alerts, context menus, and sheets, already adjust for the fold and the camera. The content you place in them stays clear of the reserved regions, so use those views when you can.

Scrolling containers, such as lists, tables, scroll views, and collection views, don’t split their content around a division by default. When the device is partially open, a row or item can run across the fold. If that makes your content harder to read or use, check for division regions and arrange the content yourself.

If your custom view arranges two related views around the fold, use an [`ArrangementView`](./arrangementview.md) instead of reading regions yourself. A split arrangement places the two views side by side or one above the other, and keeps them on separate sides of the fold. An overlay arrangement layers one view over the other, and moves them to separate sides of the fold when the device is partially open. Place an arrangement view outside navigation split views, lists, scroll views, and other containers that could make part of your view inaccessible.

Check for reserved regions yourself in custom views where controls or other important content might end up in the fold or near the camera. For example, check in a custom overlay, a floating control, or a view that positions its content with explicit frames or a custom [`Layout`](./layout.md). Check in the view that positions the content, so the frames you read use the same coordinates as the content you place.

## Include inactive regions

A reserved region can become active or inactive as conditions change. An active region currently affects your view. An inactive region doesn’t. For example, the fold of iPhone Duo becomes active when the device is partially open, and inactive again when it’s fully open. The inner camera is active only while the camera is in use, and the outer camera is always active.

By default, [`reservedRegions(kind:options:layoutDirectionBehavior:)`](./geometryproxy/reservedregions%28kind,options,layoutdirectionbehavior%29.md) returns only the active regions. To also get the inactive regions, pass [`includeInactive`](./reservedregion/queryoptions/includeinactive.md) for the `options` parameter:

```swift
let regions = proxy.reservedRegions(
    kind: .occlusion,
    options: .includeInactive)
```

Check the [`isActive`](./reservedregion/isactive.md) property of each region to find out whether it currently affects your view. An inactive region still has a frame, so you can leave room for it. This keeps your layout from jumping when the region becomes active, such as when someone folds the device or starts using the inner camera.

## Account for right-to-left layouts

With some right-to-left languages, SwiftUI flips the left and right sides of a layout. To keep reserved regions consistent with the flipped layout, the system mirrors the frames of reserved regions by default before it gives them to you. Mirrored frames match the flipped layout, so a layout that flips automatically, such as a custom [`Layout`](./layout.md), lines up with the mirrored frames without extra work. You don’t need to check the layout direction to find out whether a view overlaps a region.

If you position content in a way that doesn’t flip with the layout direction, you can get the unmirrored frames instead. Pass [`LayoutDirectionBehavior.fixed`](./layoutdirectionbehavior/fixed.md) for the `layoutDirectionBehavior` parameter:

```swift
let regions = proxy.reservedRegions(
    kind: .occlusion,
    layoutDirectionBehavior: .fixed)
```

## Track a reserved region over time

Each reserved region has an [`ReservedRegion.ID`](./reservedregion/id-swift.struct.md) that identifies it across queries. Use the ID to tell whether a region you saw in an earlier query is still there or is a different region. Because [`ReservedRegion`](./reservedregion.md) conforms to `Identifiable`, you can also pass regions directly to a [`ForEach`](./foreach.md) to create a view for each one.

For more information about preparing your app for a device with a folding display, see [Preparing your app for iPhone Duo](../TechnologyOverviews/preparing-your-app-for-iphone-duo.md). For design guidance, see Human Interface Guidelines > [Layout](https://developer.apple.com/design/human-interface-guidelines/layout).

## Topics

### Getting the region’s identity and kind
- [var id: ReservedRegion.ID](./reservedregion/id-swift.property.md)
  The identifier of the region.
- [ReservedRegion.ID](./reservedregion/id-swift.struct.md)
  An identifier for a reserved region.
- [var kind: ReservedRegion.Kind](./reservedregion/kind-swift.property.md)
  The kind of the region.
- [ReservedRegion.Kind](./reservedregion/kind-swift.struct.md)
  A kind of reserved region.
### Getting the region’s geometry
- [var frame: CGRect](./reservedregion/frame.md)
  The rectangle that describes the region within your view.
- [var margins: EdgeInsets](./reservedregion/margins.md)
  The extra space around the reserved area that keeps interactive content clear of it.
### Checking whether a region is active
- [var isActive: Bool](./reservedregion/isactive.md)
  A Boolean value that indicates whether the region is active.
### Querying reserved regions
- [ReservedRegion.QueryOptions](./reservedregion/queryoptions.md)
  Options for querying reserved regions.
### Default Implementations
- [Identifiable Implementations](./reservedregion/identifiable-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/copyable.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomReflectable](../Swift/customreflectable.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Escapable](../Swift/escapable.md)
- [Hashable](../Swift/hashable.md)
- [Identifiable](../Swift/identifiable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Measuring a view
- [struct GeometryReader](./geometryreader.md)
  A container view that defines its content as a function of its own size and coordinate space.
- [struct GeometryReader3D](./geometryreader3d.md)
  A container view that defines its content as a function of its own size and coordinate space.
- [struct GeometryProxy](./geometryproxy.md)
  A proxy for access to the size and coordinate space (for anchor resolution) of the container view.
- [func reservedRegions(kind: ReservedRegion.Kind, options: ReservedRegion.QueryOptions, layoutDirectionBehavior: LayoutDirectionBehavior) -> [ReservedRegion]](./geometryproxy/reservedregions%28kind,options,layoutdirectionbehavior%29.md)
  Returns an array of reserved regions that match the selection options you specify.
- [struct GeometryProxy3D](./geometryproxy3d.md)
  A proxy for access to the size and coordinate space of the container view.
- [func coordinateSpace(NamedCoordinateSpace) -> some View](./view/coordinatespace%28_%29.md)
  Assigns a name to the view’s coordinate space, so other code can operate on dimensions like points and sizes relative to the named space.
- [enum CoordinateSpace](./coordinatespace.md)
  A resolved coordinate space created by the coordinate space protocol.
- [protocol CoordinateSpaceProtocol](./coordinatespaceprotocol.md)
  A frame of reference within the layout system.
- [struct PhysicalMetric](./physicalmetric.md)
  Provides access to a value in points that corresponds to the specified physical measurement.
- [struct PhysicalMetricsConverter](./physicalmetricsconverter.md)
  A physical metrics converter provides conversion between point values and their extent in 3D space, in the form of physical length measurements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/reservedregion)*