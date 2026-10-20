# participantNameByIdentifier

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
var participantNameByIdentifier: [String : PersonNameComponents] { get set }
```

```objc
@property (nonatomic, copy, readwrite) NSDictionary<NSString *,NSPersonNameComponents *> * participantNameByIdentifier;
```

## See Also

### Getting conversation participants
- [var selfIdentifiers: Set<String>](./selfidentifiers.md)
  A set of strings that identifies the active person in the conversation on the current device.
- [var responsePrimaryRecipientIdentifiers: Set<String>](./responseprimaryrecipientidentifiers.md)
  A dictionary that relates participant identifiers to participant names.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiconversationcontext/participantnamebyidentifier)*