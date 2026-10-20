# animatesDrop

**Framework**: MapKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value indicating whether the annotation view is animated onto the screen.

**Availability**:
- iOS 3.0+ - Deprecated in 16.0 (renamed: MKMarkerAnnotationView)
- iPadOS 3.0+ - Deprecated in 16.0 (renamed: MKMarkerAnnotationView)
- Mac Catalyst 13.1+ - Deprecated in 16.0 (renamed: MKMarkerAnnotationView)
- macOS 10.9+ - Deprecated in 13.0 (renamed: MKMarkerAnnotationView)
- tvOS 9.2+ - Deprecated in 16.0 (renamed: MKMarkerAnnotationView)
- visionOS 1.0+ - Deprecated in 1.0 (renamed: MKMarkerAnnotationView)

## Declaration

```swift
var animatesDrop: Bool { get set }
```

```objc
@property (nonatomic) BOOL animatesDrop;
```

#### Discussion

When this property is [`true`](../../Swift/true.md), the map view animates the appearance of pin annotation views by making them appear to drop onto the map at the target point. This animation occurs whenever the view transitions from offscreen to onscreen.

## See Also

### Getting and Setting Attributes
- [var pinTintColor: UIColor!](./pintintcolor.md)
  The color of the pin head.
- [var pinColor: MKPinAnnotationColor](./pincolor.md)
  The color of the pin head.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkpinannotationview/animatesdrop)*