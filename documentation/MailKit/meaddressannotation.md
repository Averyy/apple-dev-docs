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

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)

## See Also

- [func annotateAddressesForSession(MEComposeSession, completion: ([MEEmailAddress : MEAddressAnnotation]) -> Void)](mecomposesessionhandler/annotateaddressesforsession(_:completion:).md)
  Indicates whether recipients in the compose window are valid or not.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mailkit/meaddressannotation)*