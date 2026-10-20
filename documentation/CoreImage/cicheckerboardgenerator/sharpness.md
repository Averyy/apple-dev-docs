# sharpness

**Framework**: Core Image  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

The sharpness of the edges in the pattern.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```swift
var sharpness: Float { get set }
```

```objc
@property (nonatomic) float sharpness;
```

#### Discussion

The smaller the value, the more blurry the pattern. Values range from 0.0 to 1.0.

## See Also

### Instance Properties
- [var center: CGPoint](./center.md)
  The center of the effect as x and y coordinates.
- [var color0: CIColor](./color0.md)
  A color to use for the first set of squares.
- [var color1: CIColor](./color1.md)
  A color to use for the second set of squares.
- [var width: Float](./width.md)
  The width of the squares in the pattern.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cicheckerboardgenerator/sharpness)*