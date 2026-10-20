# responseSubject

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A string that contains the subject line of an intended response.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+

## Declaration

```swift
var responseSubject: String { get set }
```

```objc
@property (nonatomic, copy, readwrite) NSString * responseSubject;
```

## See Also

### Getting message details
- [var responseHasCustomSignature: Bool](./responsehascustomsignature.md)
  A Boolean value that indicates whether the intended response contains a custom signature.
- [var responseSecondaryRecipientIdentifiers: Set<String>](./responsesecondaryrecipientidentifiers.md)
  A set of strings that identifies the secondary recipients of the message, such as those in CC or BCC messages.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uimailconversationcontext/responsesubject)*