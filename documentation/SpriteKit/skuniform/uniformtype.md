# uniformType

**Framework**: SpriteKit  
**Kind**: property

The uniform object’s data type.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var uniformType: SKUniformType { get }
```

#### Discussion

A uniform object’s type is set to [`SKUniformType.none`](skuniformtype/none.md) until the first time that the uniform variable’s value is set; this happens automatically if you use an initialization method that provides an initial type and value. Once the uniform object is given an initial value, its type changes to that value’s type and thereafter cannot be changed.

## See Also

- [var name: String](skuniform/name.md)
  The uniform’s name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skuniform/uniformtype)*