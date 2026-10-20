# disbursementCardUnsupportedError()

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: method  
**Role**: Type Method

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

```objc
+ (NSError *) disbursementCardUnsupportedError;
```

#### Return Value

An [`NSError`](../../Foundation/nserror.md) that describes the error condition.

## See Also

### Handling errors
- [class func disbursementContactInvalidError(withContactField: PKContactField, localizedDescription: String?) -> any Error](./disbursementcontactinvaliderror%28withcontactfield,localizeddescription%29.md)
  Creates a recipient contact error with the supplied field.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkdisbursementrequest/disbursementcardunsupportederror())*