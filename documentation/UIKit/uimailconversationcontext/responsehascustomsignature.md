# responseHasCustomSignature

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the intended response contains a custom signature.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+

## Declaration

```swift
var responseHasCustomSignature: Bool { get set }
```

```objc
@property (nonatomic, assign, readwrite) BOOL responseHasCustomSignature;
```

## See Also

### Getting message details
- [var responseSubject: String](./responsesubject.md)
  A string that contains the subject line of an intended response.
- [var responseSecondaryRecipientIdentifiers: Set<String>](./responsesecondaryrecipientidentifiers.md)
  A set of strings that identifies the secondary recipients of the message, such as those in CC or BCC messages.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uimailconversationcontext/responsehascustomsignature)*