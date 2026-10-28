# mesh

**Framework**: Core Image  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

An array that describes the mesh to render.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```swift
var mesh: [Any] { get set }
```

```objc
@property (nonatomic, retain) NSArray * mesh;
```

## Discussion

Specify the mesh as an array of line segments. Each line segment is stored as a [`CIVector`](../civector.md) instance that describes the line as a start point and an end point.

## See Also

### Instance Properties
- [var color: CIColor](./color.md)
  The color of the rendered mesh.
- [var width: Float](./width.md)
  The width of the effect.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cimeshgenerator/mesh)*