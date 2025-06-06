# disbursementCardUnsupportedError()

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: method

Creates an error that indicates that the selected payment pass doesn’t support receiving funds through disbursements.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 15.0+
- visionOS 1.0+

## Declaration

```swift
class func disbursementCardUnsupportedError() -> any Error
```

#### Return Value

An [`NSError`](https://developer.apple.com/documentation/Foundation/NSError) that describes the error condition.

## See Also

- [class func disbursementContactInvalidError(withContactField: PKContactField, localizedDescription: String?) -> any Error](pkdisbursementrequest/disbursementcontactinvaliderror(withcontactfield:localizeddescription:).md)
  Creates a recipient contact error with the supplied field.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkdisbursementrequest/disbursementcardunsupportederror())*