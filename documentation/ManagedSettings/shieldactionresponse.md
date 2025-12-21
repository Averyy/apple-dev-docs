# ShieldActionResponse

**Framework**: ManagedSettings  
**Kind**: enum

Constants your extension that handles shield actions can use to tell the system how to respond to an action.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+

## Declaration

```swift
enum ShieldActionResponse
```

## Topics

### Responses
- [ShieldActionResponse.close](shieldactionresponse/close.md)
  An instruction for the system to close the current application or web browser.
- [ShieldActionResponse.defer](shieldactionresponse/defer.md)
  An instruction to defer a response to the action.
- [ShieldActionResponse.none](shieldactionresponse/none.md)
  An instruction that the system doesn’t need to take any additional action on behalf of the extension.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)

## See Also

- [enum ShieldAction](shieldaction.md)
  Constants that describe a user’s action for your extension to handle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/managedsettings/shieldactionresponse)*