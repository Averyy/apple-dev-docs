# ReservedRegion.Kind

**Framework**: SwiftUI  
**Kind**: struct  
**Role**: Structure

A kind of reserved region.

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
struct Kind
```

## Overview

Pass a kind to [`reservedRegions(kind:options:layoutDirectionBehavior:)`](../geometryproxy/reservedregions%28kind,options,layoutdirectionbehavior%29.md) to choose which regions you get: [`occlusion`](./kind-swift.struct/occlusion.md) for areas that cover your content, and [`division`](./kind-swift.struct/division.md) for areas that split it. Each [`ReservedRegion`](../reservedregion.md) also reports its kind in its [`kind`](./kind-swift.property.md) property.

## Topics

### Getting reserved region kinds
- [static var occlusion: ReservedRegion.Kind](./kind-swift.struct/occlusion.md)
  A region that covers part of your view.
- [static var division: ReservedRegion.Kind](./kind-swift.struct/division.md)
  A region that splits your view into separate parts.

## Relationships

### Conforms To
- [Copyable](../../Swift/copyable.md)
- [CustomDebugStringConvertible](../../Swift/customdebugstringconvertible.md)
- [CustomReflectable](../../Swift/customreflectable.md)
- [CustomStringConvertible](../../Swift/customstringconvertible.md)
- [Equatable](../../Swift/equatable.md)
- [Escapable](../../Swift/escapable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Inspecting reserved regions
- [func reservedRegions(kind: ReservedRegion.Kind, options: ReservedRegion.QueryOptions, layoutDirectionBehavior: LayoutDirectionBehavior) -> [ReservedRegion]](../geometryproxy/reservedregions%28kind,options,layoutdirectionbehavior%29.md)
  Returns an array of reserved regions that match the selection options you specify.
- [struct ReservedRegion](../reservedregion.md)
  A region within a view’s coordinate space that another entity reserves.
- [ReservedRegion.QueryOptions](./queryoptions.md)
  Options for querying reserved regions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/reservedregion/kind-swift.struct)*