# initWithPolygon:

**Framework**: MapKit  
**Kind**: method  
**Role**: Instance Method

Initializes and returns a new overlay view using the specified polygon overlay object.

**Availability**:
- iOS 4.0+ - Deprecated in 7.0
- iPadOS 4.0+ - Deprecated in 7.0
- Mac Catalyst 13.1+ - Deprecated in 13.1

> **Deprecated**: Use an [`MKPolygonRenderer`](../mkpolygonrenderer.md) object instead.

## Declaration

```objc
- (instancetype) initWithPolygon:(MKPolygon *) polygon;
```

#### Return Value

A new polygon overlay view.

## Parameters

- `polygon`: The polygon overlay containing the information about the area to be drawn. This object must have at least three points defining the polygon in order for this view to draw the corresponding path.

## See Also

### Related Documentation
- [Location and Maps Programming Guide](https://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/LocationAwarenessPG/Introduction/Introduction.html#//apple_ref/doc/uid/TP40009497)


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkpolygonview/initwithpolygon:)*