# init(target:action:)

**Framework**: AppKit  
**Kind**: init  
**Role**: Initializer

The action is sent to the target on interaction.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.12+

## Declaration

```swift
init(target: Any?, action: Selector)
```

```objc
+ (NSSliderAccessoryBehavior *) behaviorWithTarget:(id) target action:(SEL) action;
```

## Parameters

- `target`: An optional `NSSliderAccessory`.

## See Also

### Initializers
- [init(handler: (NSSliderAccessory) -> Void)](./init%28handler%29.md)
  The handler block is invoked on interaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsslideraccessorybehavior/init(target:action:))*