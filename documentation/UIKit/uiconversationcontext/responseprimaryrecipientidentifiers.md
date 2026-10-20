# responsePrimaryRecipientIdentifiers

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A dictionary that relates participant identifiers to participant names.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+

## Declaration

```swift
var responsePrimaryRecipientIdentifiers: Set<String> { get set }
```

```objc
@property (nonatomic, copy, readwrite) NSSet<NSString *> * responsePrimaryRecipientIdentifiers;
```

## See Also

### Getting conversation participants
- [var selfIdentifiers: Set<String>](./selfidentifiers.md)
  A set of strings that identifies the active person in the conversation on the current device.
- [var participantNameByIdentifier: [String : PersonNameComponents]](./participantnamebyidentifier.md)
  A dictionary that relates participant identifiers to participant names.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiconversationcontext/responseprimaryrecipientidentifiers)*