# lineLength

**Framework**: SpriteKit  
**Kind**: property  
**Role**: Instance Property

The length of the line defined by the shape node.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
var lineLength: CGFloat { get }
```

```objc
@property (nonatomic, readonly) CGFloat lineLength;
```

## Discussion

This property takes effect only when the shape has a stroke. The valid range is between `[0.1]` where one indicates that the shape is fully stroked, and zero indicates that the shape is not stroked at all. By interpolating this value over time (for example, in your scene’s [`update(_:)`](../skscene/update%28_%29.md) callback), you can animate the shape as if it were drawn in real time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skshapenode/linelength)*