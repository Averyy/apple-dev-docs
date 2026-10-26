# initWithOverlay:

**Framework**: MapKit  
**Kind**: method  
**Role**: Instance Method

Initializes and returns the overlay view and associates it with the specified overlay object.

**Availability**:
- iOS 4.0+ - Deprecated in 7.0
- iPadOS 4.0+ - Deprecated in 7.0
- Mac Catalyst 13.1+ - Deprecated in 13.1

> **Deprecated**: Use an [`MKOverlayRenderer`](../mkoverlayrenderer.md) object instead.

## Declaration

```objc
- (instancetype) initWithOverlay:(id<MKOverlay>) overlay;
```

#### Return Value

An initialized overlay object.

#### Discussion

Upon initialization, the frame of the overlay view is set to [`CGRectZero`](../../CoreGraphics/cgrectzero.md). The map view sets the size and position of the view at display time, and you should not change those values yourself.

## Parameters

- `overlay`: The overlay object to use when drawing the overlay on the map. This object provides the data needed to draw the overlay’s shape. This object is retained by the overlay view.

## See Also

### Related Documentation
- [Location and Maps Programming Guide](https://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/LocationAwarenessPG/Introduction/Introduction.html#//apple_ref/doc/uid/TP40009497)


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkoverlayview/initwithoverlay:)*