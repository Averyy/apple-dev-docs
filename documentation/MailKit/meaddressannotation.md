# MEAddressAnnotation

**Framework**: MailKit  
**Kind**: class

An object that indicates the validity of an email address.

**Availability**:
- macOS 12.0+

## Declaration

```swift
class MEAddressAnnotation
```

#### Overview

Mail displays the status of an annotation as part of the address tokens in the To, Cc, and Bcc fields using a status icon and color.

## Topics

### Specifying Email Address Validity
- [class func success(withLocalizedDescription: String) -> MEAddressAnnotation](meaddressannotation/success(withlocalizeddescription:).md)
  Indicates an address is valid and correct.
- [class func warning(withLocalizedDescription: String) -> MEAddressAnnotation](meaddressannotation/warning(withlocalizeddescription:).md)
  Indicates an address may be invalid or needs attention.
- [class func error(withLocalizedDescription: String) -> MEAddressAnnotation](meaddressannotation/error(withlocalizeddescription:).md)
  Indicates an address is invalid and may result in failure to deliver a message.
### Initializers
- [init?(coder: NSCoder)](meaddressannotation/init(coder:).md)

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSCoding](../foundation/nscoding.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [NSSecureCoding](../foundation/nssecurecoding.md)

## See Also

- [func annotateAddressesForSession(MEComposeSession, completion: ([MEEmailAddress : MEAddressAnnotation]) -> Void)](mecomposesessionhandler/annotateaddressesforsession(_:completion:).md)
  Indicates whether recipients in the compose window are valid or not.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mailkit/meaddressannotation)*