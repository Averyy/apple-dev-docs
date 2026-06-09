# PKFloatRange

**Framework**: PencilKit  
**Kind**: class

A utility class that represents range components of a stroke.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
@interface PKFloatRange : NSObject
```

## Topics

### Creating a new range
- [- initWithLowerBound:upperBound:](pkfloatrange/initwithlowerbound:upperbound:.md)
  A utility class used to contain ranges returned by the PKStroke API.
### Getting the boundaries of the range
- [lowerBound](pkfloatrange/lowerbound.md)
  A floating point value that represents the lower bound of the range.
- [upperBound](pkfloatrange/upperbound.md)
  A floating point value that represents the upper bound of the range.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [NSCopying](../Foundation/NSCopying.md)

## See Also

- [class PKCanvasView](pkcanvasview.md)
  A view that captures Apple Pencil input and displays the rendered results in an iOS app.
- [class PKDrawingReference](pkdrawingreference.md)
  A data structure that contains the drawing information captured by a canvas view.
- [class PKStrokeReference](pkstrokereference.md)
  A class that represents the paths, boundaries and other properties of a stroke drawn on a canvas.
- [class PKStrokePathReference](pkstrokepathreference.md)
  A class that captures the components of a stroke and provides methods to find and interpolate points along the stroke’s path.
- [class PKStrokePointReference](pkstrokepointreference.md)
  A class that represents the properties of a specific point along a stroke’s path.
- [class PKInkReference](pkinkreference.md)
  Provides a description of the creation and rendering of marks on a canvas.
- [PKStrokeRenderState](pkstrokerenderstate.md)
  An object that captures the render-time state of a stroke, such as grain texture position.
- [class PKConvertedBezierPointReference](pkconvertedbezierpointreference.md)
  An object that provides information about a B-spline control point converted from a Bézier path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pencilkit/pkfloatrange)*