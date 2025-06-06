# init(annotation:reuseIdentifier:)

**Framework**: MapKit  
**Kind**: init

Creates and returns a new annotation view.

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
init(annotation: (any MKAnnotation)?, reuseIdentifier: String?)
```

#### Return Value

The initialized annotation view, or `nil` if there’s a problem initializing the object.

#### Discussion

The reuse identifier provides a way for you to improve performance by recycling annotation views as the map scrolls on and off of the map. As MapKit no longer needs views, the map view moves them to a reuse queue. When a new annotation becomes visible, your app can request a view for that annotation by passing the appropriate reuse identifier string to the [`dequeueReusableAnnotationView(withIdentifier:)`](mkmapview/dequeuereusableannotationview(withidentifier:).md) method of [`MKMapView`](mkmapview.md).

## Parameters

- `annotation`: The annotation object to associate with the new view.
- `reuseIdentifier`: If you plan to reuse the annotation view for similar types of annotations, pass a string to identify it. Although you can pass   if you don’t intend to reuse the view, reusing annotation views is generally best practice.

## See Also

- [Location and Maps Programming Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/LocationAwarenessPG/Introduction/Introduction.html#//apple_ref/doc/uid/TP40009497)
- [init?(coder: NSCoder)](mkannotationview/init(coder:).md)
  Creates an annotation view using data from the specified unarchiver.
- [func prepareForReuse()](mkannotationview/prepareforreuse.md)
  Calls this method when removing the view from the reuse queue.
- [func prepareForDisplay()](mkannotationview/preparefordisplay.md)
  Notifies the annotation view that the map view is about to display it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkannotationview/init(annotation:reuseidentifier:))*