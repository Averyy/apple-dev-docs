# disbursementContactInvalidError(withContactField:localizedDescription:)

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: method  
**Role**: Type Method

Creates a recipient contact error with the supplied field.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 15.0+
- visionOS 1.0+

## Declaration

```swift
class func disbursementContactInvalidError(withContactField field: PKContactField, localizedDescription: String?) -> any Error
```

```objc
+ (NSError *) disbursementContactInvalidErrorWithContactField:(PKContactField) field localizedDescription:(NSString *) localizedDescription;
```

## Return Value

An [`NSError`](../../Foundation/nserror.md) object.

## Discussion

There’s limited display space available for descriptions, so keep your messages concise.

## Parameters

- `field`: The [`PKContactField`](../pkcontactfield.md) that contains the error.
- `localizedDescription`: An optional localized description that the framework displays to the individual.

## See Also

### Handling errors
- [class func disbursementCardUnsupportedError() -> any Error](./disbursementcardunsupportederror%28%29.md)
  Creates an error that indicates that the selected payment pass doesn’t support receiving funds through disbursements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkdisbursementrequest/disbursementcontactinvaliderror(withcontactfield:localizeddescription:))*