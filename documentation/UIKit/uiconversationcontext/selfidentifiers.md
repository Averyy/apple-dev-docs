# selfIdentifiers

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A set of strings that identifies the active person in the conversation on the current device.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+

## Declaration

```swift
var selfIdentifiers: Set<String> { get set }
```

```objc
@property (nonatomic, copy, readwrite) NSSet<NSString *> * selfIdentifiers;
```

## See Also

### Getting conversation participants
- [var responsePrimaryRecipientIdentifiers: Set<String>](./responseprimaryrecipientidentifiers.md)
  A dictionary that relates participant identifiers to participant names.
- [var participantNameByIdentifier: [String : PersonNameComponents]](./participantnamebyidentifier.md)
  A dictionary that relates participant identifiers to participant names.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiconversationcontext/selfidentifiers)*