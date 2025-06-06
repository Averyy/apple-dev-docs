# success(withLocalizedDescription:)

**Framework**: MailKit  
**Kind**: method

Indicates an address is valid and correct.

**Availability**:
- macOS 12.0+

## Declaration

```swift
class func success(withLocalizedDescription localizedDescription: String) -> MEAddressAnnotation
```

#### Return Value

An annotation that indicates an email address is valid.

## Parameters

- `localizedDescription`: A user-visible string with details about the address, such as the full name of the recipient.

## See Also

- [class func warning(withLocalizedDescription: String) -> MEAddressAnnotation](meaddressannotation/warning(withlocalizeddescription:).md)
  Indicates an address may be invalid or needs attention.
- [class func error(withLocalizedDescription: String) -> MEAddressAnnotation](meaddressannotation/error(withlocalizeddescription:).md)
  Indicates an address is invalid and may result in failure to deliver a message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mailkit/meaddressannotation/success(withlocalizeddescription:))*