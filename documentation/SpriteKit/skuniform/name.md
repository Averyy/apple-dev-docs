# name

**Framework**: SpriteKit  
**Kind**: property  
**Role**: Instance Property

The uniform’s name.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var name: String { get }
```

```objc
@property (nonatomic, readonly) NSString * name;
```

## Discussion

Your custom fragment shader uses this name to identify the variable. SpriteKit automatically declares the uniform variable for your shader.

## See Also

### Reading Information About a Uniform
- [var uniformType: SKUniformType](./uniformtype.md)
  The uniform object’s data type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skuniform/name)*