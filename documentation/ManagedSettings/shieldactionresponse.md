# ShieldActionResponse

**Framework**: Managed Settings  
**Kind**: enum  
**Role**: Enumeration

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
- [ShieldActionResponse.close](./shieldactionresponse/close.md)
  An instruction for the system to close the current application or web browser.
- [ShieldActionResponse.defer](./shieldactionresponse/defer.md)
  An instruction to defer a response to the action.
- [ShieldActionResponse.none](./shieldactionresponse/none.md)
  An instruction that the system doesn’t need to take any additional action on behalf of the extension.
### Enumeration Cases
- [ShieldActionResponse.openParentalControlsApp](./shieldactionresponse/openparentalcontrolsapp.md)
  An instruction for the system to open your parental controls app that is responsible for shielding the application or web browser

## Relationships

### Conforms To
- [Copyable](../Swift/copyable.md)
- [Equatable](../Swift/equatable.md)
- [Escapable](../Swift/escapable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)

## See Also

### Handling shield actions
- [enum ShieldAction](./shieldaction.md)
  Constants that describe a user’s action for your extension to handle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/managedsettings/shieldactionresponse)*