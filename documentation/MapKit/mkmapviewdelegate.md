# MKMapViewDelegate

**Framework**: MapKit  
**Kind**: protocol  
**Role**: Protocol

Optional methods that you use to receive map-related update messages.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```swift
@MainActor
protocol MKMapViewDelegate : NSObjectProtocol
```

```objc
@protocol MKMapViewDelegate <NSObject>
```

## Overview

Because many map operations require the [`MKMapView`](./mkmapview.md) class to load data asynchronously, the map view calls these methods to notify your app when specific operations complete. The map view also uses these methods to request annotation and overlay views, and to manage interactions with those views.

Before releasing an [`MKMapView`](./mkmapview.md) object that you set a delegate for, remember to set that object’s [`delegate`](./mkmapview/delegate.md) property to `nil`. MapKit calls all of your delegate methods on the app’s main thread.

## Topics

### Responding to map position changes
- [func mapView(MKMapView, regionWillChangeAnimated: Bool)](./mkmapviewdelegate/mapview%28_,regionwillchangeanimated%29.md)
  Tells the delegate when the region the map view is displaying is about to change.
- [func mapViewDidChangeVisibleRegion(MKMapView)](./mkmapviewdelegate/mapviewdidchangevisibleregion%28_%29.md)
  Tells the delegate when the map view’s visible region changes.
- [func mapView(MKMapView, regionDidChangeAnimated: Bool)](./mkmapviewdelegate/mapview%28_,regiondidchangeanimated%29.md)
  Tells the delegate when the region the map view is displaying changes.
### Loading the map data
- [func mapViewWillStartLoadingMap(MKMapView)](./mkmapviewdelegate/mapviewwillstartloadingmap%28_%29.md)
  Tells the delegate that the specified map view is about to retrieve some map data.
- [func mapViewDidFinishLoadingMap(MKMapView)](./mkmapviewdelegate/mapviewdidfinishloadingmap%28_%29.md)
  Tells the delegate when the specified map view successfully loads the needed map data.
- [func mapViewDidFailLoadingMap(MKMapView, withError: any Error)](./mkmapviewdelegate/mapviewdidfailloadingmap%28_,witherror%29.md)
  Tells the delegate that the specified view is unable to load the map data.
- [func mapViewWillStartRenderingMap(MKMapView)](./mkmapviewdelegate/mapviewwillstartrenderingmap%28_%29.md)
  Tells the delegate that the map view is about to start rendering some of its tiles.
- [func mapViewDidFinishRenderingMap(MKMapView, fullyRendered: Bool)](./mkmapviewdelegate/mapviewdidfinishrenderingmap%28_,fullyrendered%29.md)
  Tells the delegate when the map view finishes rendering all visible tiles.
### Tracking the user’s location
- [func mapViewWillStartLocatingUser(MKMapView)](./mkmapviewdelegate/mapviewwillstartlocatinguser%28_%29.md)
  Tells the delegate that the map view is about to start tracking the user’s location.
- [func mapViewDidStopLocatingUser(MKMapView)](./mkmapviewdelegate/mapviewdidstoplocatinguser%28_%29.md)
  Tells the delegate when the map view stops tracking the user’s location.
- [func mapView(MKMapView, didUpdate: MKUserLocation)](./mkmapviewdelegate/mapview%28_,didupdate%29.md)
  Tells the delegate when the map view updates the user’s location.
- [func mapView(MKMapView, didFailToLocateUserWithError: any Error)](./mkmapviewdelegate/mapview%28_,didfailtolocateuserwitherror%29.md)
  Tells the delegate when an attempt to locate the user’s location fails.
- [func mapView(MKMapView, didChange: MKUserTrackingMode, animated: Bool)](./mkmapviewdelegate/mapview%28_,didchange,animated%29.md)
  Tells the delegate when the user-tracking mode changes.
### Managing annotation views
- [func mapView(MKMapView, viewFor: any MKAnnotation) -> MKAnnotationView?](./mkmapviewdelegate/mapview%28_,viewfor%29-8humz.md)
  Returns the view associated with the specified annotation object.
- [func mapView(MKMapView, didAdd: [MKAnnotationView])](./mkmapviewdelegate/mapview%28_,didadd%29-44xon.md)
  Tells the delegate when the map view adds one or more annotation views to the map.
- [func mapView(MKMapView, annotationView: MKAnnotationView, calloutAccessoryControlTapped: UIControl)](./mkmapviewdelegate/mapview%28_,annotationview,calloutaccessorycontroltapped%29.md)
  Tells the delegate when the user taps one of the annotation view’s accessory buttons.
- [func mapView(MKMapView, clusterAnnotationForMemberAnnotations: [any MKAnnotation]) -> MKClusterAnnotation](./mkmapviewdelegate/mapview%28_,clusterannotationformemberannotations%29.md)
  Asks the delegate to provide a cluster annotation object for the specified annotations.
### Dragging an annotation view
- [func mapView(MKMapView, annotationView: MKAnnotationView, didChange: MKAnnotationView.DragState, fromOldState: MKAnnotationView.DragState)](./mkmapviewdelegate/mapview%28_,annotationview,didchange,fromoldstate%29.md)
  Tells the delegate when the drag state of one of its annotation views changes.
### Selecting annotations and annotations views
- [func mapView(MKMapView, didSelect: MKAnnotationView)](./mkmapviewdelegate/mapview%28_,didselect%29-41by3.md)
  Tells the delegate when the user selects one or more of its annotation views.
- [func mapView(MKMapView, didDeselect: MKAnnotationView)](./mkmapviewdelegate/mapview%28_,diddeselect%29-yo7q.md)
  Tells the delegate when the user deselects one or more of its annotation views.
- [func mapView(MKMapView, didDeselect: any MKAnnotation)](./mkmapviewdelegate/mapview%28_,diddeselect%29-4ldss.md)
  Tells the delegate when the user deselects one or more annotations.
- [func mapView(MKMapView, didSelect: any MKAnnotation)](./mkmapviewdelegate/mapview%28_,didselect%29-9km43.md)
  Tells the delegate when the user selects one or more annotations.
- [var selectableMapFeatures: MKMapFeatureOptions](./mkmapview/selectablemapfeatures.md)
  The property that describes which selectable features the map responds to.
### Managing the display of overlays
- [func mapView(MKMapView, selectionAccessoryFor: any MKAnnotation) -> MKSelectionAccessory?](./mkmapviewdelegate/mapview%28_,selectionaccessoryfor%29.md)
  Specifies the accessory to display for a selected annotation
- [func mapView(MKMapView, rendererFor: any MKOverlay) -> MKOverlayRenderer](./mkmapviewdelegate/mapview%28_,rendererfor%29.md)
  Asks the delegate for a renderer object to use when drawing the specified overlay.
- [func mapView(MKMapView, didAdd: [MKOverlayRenderer])](./mkmapviewdelegate/mapview%28_,didadd%29-793gj.md)
  Tells the delegate when the map view adds one or more renderer objects to the map.
- [func mapView(MKMapView, viewFor: any MKOverlay) -> MKOverlayView](./mkmapviewdelegate/mapview%28_,viewfor%29-6j267.md)
  Asks the delegate for the overlay view to use when displaying the specified overlay object.
- [func mapView(MKMapView, didAddOverlayViews: [Any])](./mkmapviewdelegate/mapview%28_,didaddoverlayviews%29.md)
  Tells the delegate when the map adds one or more overlay views to the map.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Customizing the map view behavior
- [var delegate: (any MKMapViewDelegate)?](./mkmapview/delegate.md)
  The receiver’s delegate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmapviewdelegate)*