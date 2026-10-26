# initWithPolyline:

**Framework**: MapKit  
**Kind**: method  
**Role**: Instance Method

Initializes and returns a new overlay view using the specified polyline overlay object

**Availability**:
- iOS 4.0+ - Deprecated in 7.0
- iPadOS 4.0+ - Deprecated in 7.0
- Mac Catalyst 13.1+ - Deprecated in 13.1

> **Deprecated**: Use an [`MKPolylineRenderer`](../mkpolylinerenderer.md) object instead.

## Declaration

```objc
- (instancetype) initWithPolyline:(MKPolyline *) polyline;
```

#### Return Value

A new polyline overlay view.

## Parameters

- `polyline`: The polyline overlay object containing the information about the path to be stroked. This object must have at least two points defined in order for this view to draw the corresponding path.

## See Also

### Related Documentation
- [Location and Maps Programming Guide](https://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/LocationAwarenessPG/Introduction/Introduction.html#//apple_ref/doc/uid/TP40009497)


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkpolylineview/initwithpolyline:)*