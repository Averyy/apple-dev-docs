# MKAnnotationView

**Framework**: MapKit  
**Kind**: class

The visual representation of one of your annotation objects.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.2+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class MKAnnotationView
```

#### Overview

 are loosely coupled to a corresponding , which is an object that conforms to the [`MKAnnotation`](mkannotation.md) protocol. When an annotation’s coordinate point is in the map’s visible region, the map view asks its delegate to provide a corresponding annotation view. MapKit may recycle annotation views and put them into a reuse queue that the map view maintains.

The most efficient way to provide the content for an annotation view is to set its [`image`](mkannotationview/image.md) property. The annotation view sizes itself automatically to the image you specify and draws that image for its contents. Because it’s a view, you can also override the [`draw(_:)`](https://developer.apple.com/documentation/UIKit/UIView/draw(_:)) method and draw your view’s content manually. If you choose to override [`draw(_:)`](https://developer.apple.com/documentation/UIKit/UIView/draw(_:)) directly and you don’t specify a custom image in the [`image`](mkannotationview/image.md) property, the annotation view sets the width and height of the annotation view’s frame to `0` by default. Before the framework can draw your custom content, you need to set the width and height to nonzero values by modifying the view’s [`frame`](https://developer.apple.com/documentation/UIKit/UIView/frame) property. In general, if your content consists entirely of static images, it’s more efficient to set the [`image`](mkannotationview/image.md) property and change it as necessary than to draw the images yourself.

Annotation views anchor to the map at the point that their associated annotation object specifies. Although they scroll with the map contents, annotation views reside in a separate display layer and don’t scale when the size of the visible map region changes.

Additionally, annotation views support the concept of a , which determines whether the map displays the annotation view as unselected, selected, or selected and displaying a standard callout view. The user toggles between the selection states through interactions with the annotation view. In the unselected state, the map displays the annotation view, but doesn’t highlight it. In the selected state, the framework highlights the annotation, but doesn’t display the callout. Finally, the map view can display the annotation with both a highlight and a callout. The callout view displays additional information, such as a title string and controls for viewing more information. The annotation object provides the title information, but your annotation view is responsible for providing any custom controls. For more information, see the [`Subclassing notes`](mkannotationview#Subclassing-notes.md) section below.

##### Reuse Annotation Views

The design of annotation views enables their reuse as the user (or your app) changes the visible map region. The reuse of annotation views provides significant performance improvements during scrolling by avoiding the creation of new view objects during this time-critical operation. For this reason, don’t tightly couple annotation views to the contents of their associated annotation. Instead, use the properties of an annotation view (or setter methods) to configure the view for a new annotation object.

Whenever you initialize a new annotation view, specify a reuse identifier for that view. When the framework no longer needs annotation views, the map view may put them into a reuse queue. As the framework adds new annotations to the map view, the delegate object can then dequeue and reconfigure an existing view (rather than create a new one) using the [`dequeueReusableAnnotationView(withIdentifier:)`](mkmapview/dequeuereusableannotationview(withidentifier:).md) method of [`MKMapView`](mkmapview.md).

##### Subclassing Notes

You can use the `MKAnnotationView` class as-is or subclass it to provide custom behavior as necessary. The [`image`](mkannotationview/image.md) property of the class lets you set the appearance of the annotation view without subclassing directly. You might also create custom subclasses as a convenience and use them to put the annotation view in a known state.

There are no special requirements for subclassing `MKAnnotationView`. However, the following list includes some reasons you might want to subclass, and the methods to override to implement the desired behavior:

- To put the annotation view into a consistent state, provide a custom initialization method. Your custom initialization method then calls [`init(annotation:reuseIdentifier:)`](mkannotationview/init(annotation:reuseidentifier:).md) to initialize the superclass.
- To provide custom callout views, override the [`leftCalloutAccessoryView`](mkannotationview/leftcalloutaccessoryview.md) method and use it to return the views.

If you support draggable annotation views in iOS, your subclass is responsible for changing the value in the [`dragState`](mkannotationview/dragstate-swift.property.md) property to appropriate values at key transition points in the drag operation. For more information, see the description of that property.

## Topics

### Creating and preparing an annotation view
- [init(annotation: (any MKAnnotation)?, reuseIdentifier: String?)](mkannotationview/init(annotation:reuseidentifier:).md)
  Creates and returns a new annotation view.
- [init?(coder: NSCoder)](mkannotationview/init(coder:).md)
  Creates an annotation view using data from the specified unarchiver.
- [func prepareForReuse()](mkannotationview/prepareforreuse.md)
  Calls this method when removing the view from the reuse queue.
- [func prepareForDisplay()](mkannotationview/preparefordisplay.md)
  Notifies the annotation view that the map view is about to display it.
### Setting the priority for display
- [var displayPriority: MKFeatureDisplayPriority](mkannotationview/displaypriority.md)
  The display priority of the annotation view.
- [struct MKFeatureDisplayPriority](mkfeaturedisplaypriority.md)
  Constants that indicates the display priority for annotations.
- [var zPriority: MKAnnotationViewZPriority](mkannotationview/zpriority.md)
  The relative importance of the annotation view when in an unselected state with respect to its ordering along the z-axis.
- [var selectedZPriority: MKAnnotationViewZPriority](mkannotationview/selectedzpriority.md)
  The relative importance of the annotation view when in a selected state with respect to its ordering along the z-axis.
- [struct MKAnnotationViewZPriority](mkannotationviewzpriority.md)
  Constants that indicates the priority for ordering overlapping annotation views.
### Getting and setting attributes
- [var isEnabled: Bool](mkannotationview/isenabled.md)
  A Boolean value that indicates whether the annotation is in an enabled state.
- [var image: UIImage?](mkannotationview/image.md)
  The image the annotation view displays.
- [var isHighlighted: Bool](mkannotationview/ishighlighted.md)
  A Boolean value that indicates whether the map view highlights the annotation view.
- [var annotation: (any MKAnnotation)?](mkannotationview/annotation.md)
  The annotation object associated with the view.
- [var centerOffset: CGPoint](mkannotationview/centeroffset.md)
  The offset (in points) at which to display the view.
- [var calloutOffset: CGPoint](mkannotationview/calloutoffset.md)
  The offset (in points) at which to place the callout.
- [var reuseIdentifier: String?](mkannotationview/reuseidentifier.md)
  The string that identifies that the annotation view is reusable.
### Managing the selection state
- [func setSelected(Bool, animated: Bool)](mkannotationview/setselected(_:animated:).md)
  Sets the selection state of the annotation view.
- [var isSelected: Bool](mkannotationview/isselected.md)
  A Boolean value that indicates whether the annotation view is in a selected state.
### Managing callout views
- [var accessoryOffset: CGPoint](mkannotationview/accessoryoffset.md)
  An offset that changes the accessory’s default anchor point.
- [var canShowCallout: Bool](mkannotationview/canshowcallout.md)
  A Boolean value that indicates whether the annotation view is able to display extra information in a callout.
- [var leftCalloutAccessoryView: UIView?](mkannotationview/leftcalloutaccessoryview.md)
  The view to display on the left side of the standard callout.
- [var rightCalloutAccessoryView: UIView?](mkannotationview/rightcalloutaccessoryview.md)
  The view to display on the right side of the standard callout.
- [var detailCalloutAccessoryView: UIView?](mkannotationview/detailcalloutaccessoryview.md)
  The detail accessory view to use in the standard callout.
- [var leftCalloutOffset: CGPoint](mkannotationview/leftcalloutoffset.md)
  The offset in points from the middle-left of the annotation view.
- [var rightCalloutOffset: CGPoint](mkannotationview/rightcalloutoffset.md)
  The offset in points from the middle-right of the annotation view.
### Supporting drag operations
- [var isDraggable: Bool](mkannotationview/isdraggable.md)
  A Boolean value that indicates whether the annotation view is draggable.
- [func setDragState(MKAnnotationView.DragState, animated: Bool)](mkannotationview/setdragstate(_:animated:).md)
  Sets the drag state for the annotation view.
- [var dragState: MKAnnotationView.DragState](mkannotationview/dragstate-swift.property.md)
  The drag state of the annotation view.
### Managing collisions between annotation views
- [var collisionMode: MKAnnotationView.CollisionMode](mkannotationview/collisionmode-swift.property.md)
  The collision mode to use when interpreting the collision frame rectangle.
- [MKAnnotationView.CollisionMode](mkannotationview/collisionmode-swift.enum.md)
  Constants that indicates how to interpret the collision frame rectangle of an annotation view.
### Clustering annotation views
- [Decluttering a Map with MapKit Annotation Clustering](decluttering-a-map-with-mapkit-annotation-clustering.md)
  Enhance the readability of a map by replacing overlapping annotations with a clustering annotation view.
- [var clusteringIdentifier: String?](mkannotationview/clusteringidentifier.md)
  An identifier that determines whether the annotation view participates in clustering.
- [var cluster: MKAnnotationView?](mkannotationview/cluster.md)
  The clustering annotation view that replaces the annotation view.
### Constants
- [MKAnnotationView.DragState](mkannotationview/dragstate-swift.enum.md)
  Constants that indicate the drag state of an annotation view.

## Relationships

### Inherits From
- [NSView](../AppKit/NSView.md)
- [UIView](../UIKit/UIView.md)
### Inherited By
- [MKMarkerAnnotationView](mkmarkerannotationview.md)
- [MKPinAnnotationView](mkpinannotationview.md)
- [MKUserLocationView](mkuserlocationview.md)
### Conforms To
- [CALayerDelegate](../QuartzCore/CALayerDelegate.md)
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSAccessibilityElementProtocol](../AppKit/NSAccessibilityElementProtocol.md)
- [NSAccessibilityProtocol](../AppKit/NSAccessibilityProtocol.md)
- [NSAnimatablePropertyContainer](../AppKit/NSAnimatablePropertyContainer.md)
- [NSAppearanceCustomization](../AppKit/NSAppearanceCustomization.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSDraggingDestination](../AppKit/NSDraggingDestination.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSStandardKeyBindingResponding](../AppKit/NSStandardKeyBindingResponding.md)
- [NSTouchBarProvider](../AppKit/NSTouchBarProvider.md)
- [NSUserActivityRestoring](../AppKit/NSUserActivityRestoring.md)
- [NSUserInterfaceItemIdentification](../AppKit/NSUserInterfaceItemIdentification.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [UIAccessibilityIdentification](../UIKit/UIAccessibilityIdentification.md)
- [UIActivityItemsConfigurationProviding](../UIKit/UIActivityItemsConfigurationProviding.md)
- [UIAppearance](../UIKit/UIAppearance.md)
- [UIAppearanceContainer](../UIKit/UIAppearanceContainer.md)
- [UICoordinateSpace](../UIKit/UICoordinateSpace.md)
- [UIDynamicItem](../UIKit/UIDynamicItem.md)
- [UIFocusEnvironment](../UIKit/UIFocusEnvironment.md)
- [UIFocusItem](../UIKit/UIFocusItem.md)
- [UIFocusItemContainer](../UIKit/UIFocusItemContainer.md)
- [UILargeContentViewerItem](../UIKit/UILargeContentViewerItem.md)
- [UIPasteConfigurationSupporting](../UIKit/UIPasteConfigurationSupporting.md)
- [UIPopoverPresentationControllerSourceItem](../UIKit/UIPopoverPresentationControllerSourceItem.md)
- [UIResponderStandardEditActions](../UIKit/UIResponderStandardEditActions.md)
- [UITraitChangeObservable](../UIKit/UITraitChangeObservable-67e94.md)
- [UITraitEnvironment](../UIKit/UITraitEnvironment.md)
- [UIUserActivityRestoring](../UIKit/UIUserActivityRestoring.md)

## See Also

- [class MKPlacemark](mkplacemark.md)
  A user-friendly description of a location on the map.
- [protocol MKAnnotation](mkannotation.md)
  An interface for associating your content with a specific map location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkannotationview)*