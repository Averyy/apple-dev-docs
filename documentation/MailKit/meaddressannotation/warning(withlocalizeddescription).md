# warning(withLocalizedDescription:)

**Framework**: MailKit  
**Kind**: method

Indicates an address may be invalid or needs attention.

**Availability**:
- macOS 12.0+

## Declaration

```swift
class func warning(withLocalizedDescription localizedDescription: String) -> MEAddressAnnotation
```

#### Return Value

An annotation that indicates an email address may not be valid or needs attention.

## Parameters

- `localizedDescription`: A user-visible string with details about why the recipient needs attention.

## See Also

- [class func success(withLocalizedDescription: String) -> MEAddressAnnotation](meaddressannotation/success(withlocalizeddescription:).md)
  Indicates an address is valid and correct.
- [class func error(withLocalizedDescription: String) -> MEAddressAnnotation](meaddressannotation/error(withlocalizeddescription:).md)
  Indicates an address is invalid and may result in failure to deliver a message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mailkit/meaddressannotation/warning(withlocalizeddescription:))*