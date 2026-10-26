# sceneWithSize:

**Framework**: SpriteKit  
**Kind**: method  
**Role**: Type Method

Creates and returns a new scene object.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```objc
+ (instancetype) sceneWithSize:(CGSize) size;
```

#### Return Value

A new scene object.

#### Discussion

This class method allocates a new scene object and calls its [`init(size:)`](./init%28size%29.md) initializer method.

## Parameters

- `size`: The size of the scene in points.

## See Also

### Creating a Scene Programmatically
- [init(size: CGSize)](./init%28size%29.md)
  Initializes a new scene object.
- [var size: CGSize](./size.md)
  The dimensions of the scene, in points.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skscene/scenewithsize:)*