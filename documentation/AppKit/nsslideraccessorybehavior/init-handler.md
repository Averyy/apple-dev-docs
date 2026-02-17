# init(handler:)

**Framework**: AppKit  
**Kind**: init

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

#### Discussion

This variant is not codable and will assert in `-encodeWithCoder:`.

## See Also

- [init(target: Any?, action: Selector)](nsslideraccessorybehavior/init(target:action:).md)
  The action is sent to the target on interaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsslideraccessorybehavior/init(handler:))*