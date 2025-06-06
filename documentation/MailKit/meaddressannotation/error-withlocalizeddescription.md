# error(withLocalizedDescription:)

**Framework**: MailKit  
**Kind**: method

Indicates an address is invalid and may result in failure to deliver a message.

**Availability**:
- macOS 12.0+

## Declaration

```swift
class func error(withLocalizedDescription localizedDescription: String) -> MEAddressAnnotation
```

#### Return Value

An annotation that indicates an email address is invalid and may result in failure to deliver a message.

## Parameters

- `localizedDescription`: A user-visible string with details about the reason the address is invalid.

## See Also

- [class func success(withLocalizedDescription: String) -> MEAddressAnnotation](meaddressannotation/success(withlocalizeddescription:).md)
  Indicates an address is valid and correct.
- [class func warning(withLocalizedDescription: String) -> MEAddressAnnotation](meaddressannotation/warning(withlocalizeddescription:).md)
  Indicates an address may be invalid or needs attention.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mailkit/meaddressannotation/error(withlocalizeddescription:))*