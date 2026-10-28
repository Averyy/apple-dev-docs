# init(handler:)

**Framework**: AppKit  
**Kind**: init  
**Role**: Initializer

The handler block is invoked on interaction.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.12+

## Declaration

```swift
init(handler: @escaping (NSSliderAccessory) -> Void)
```

```objc
+ (NSSliderAccessoryBehavior *) behaviorWithHandler:(void (^)(NSSliderAccessory *)) handler;
```

## Discussion

This variant is not codable and will assert in `-encodeWithCoder:`.

## See Also

### Initializers
- [init(target: Any?, action: Selector)](./init%28target,action%29.md)
  The action is sent to the target on interaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsslideraccessorybehavior/init(handler:))*