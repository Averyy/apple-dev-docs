# color2

**Framework**: Model I/O  
**Kind**: property  
**Role**: Instance Property

The color for the other half of the squares in the checkerboard pattern.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var color2: CGColor? { get set }
```

```objc
@property (nonatomic, nullable) CGColorRef color2;
```

#### Discussion

This color appears in the second square from top left (in either direction) of the generated pattern, and in alternate squares thereafter.

Changing the [`divisions`](./divisions.md), [`color1`](./color1.md), or [`color2`](./color2.md) properties invalidates the cache, causing Model I/O to regenerate texel data the next time it is needed.

## See Also

### Configuring the Checkerboard Pattern
- [var color1: CGColor?](./color1.md)
  The color for half of the squares in the checkerboard pattern.
- [var divisions: Float](./divisions.md)
  The number of squares along each dimension in the checkerboard pattern.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlcheckerboardtexture/color2)*