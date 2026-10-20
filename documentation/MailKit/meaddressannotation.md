# MEAddressAnnotation

**Framework**: MailKit  
**Kind**: class  
**Role**: Class

An object that indicates the validity of an email address.

**Availability**:
- macOS 12.0+

## Declaration

```swift
class MEAddressAnnotation
```

```objc
@interface MEAddressAnnotation : NSObject
```

#### Overview

Mail displays the status of an annotation as part of the address tokens in the To, Cc, and Bcc fields using a status icon and color.

## Topics

### Specifying Email Address Validity
- [class func success(withLocalizedDescription: String) -> MEAddressAnnotation](./meaddressannotation/success%28withlocalizeddescription%29.md)
  Indicates an address is valid and correct.
- [class func warning(withLocalizedDescription: String) -> MEAddressAnnotation](./meaddressannotation/warning%28withlocalizeddescription%29.md)
  Indicates an address may be invalid or needs attention.
- [class func error(withLocalizedDescription: String) -> MEAddressAnnotation](./meaddressannotation/error%28withlocalizeddescription%29.md)
  Indicates an address is invalid and may result in failure to deliver a message.
### Initializers
- [init?(coder: NSCoder)](./meaddressannotation/init%28coder%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)

## See Also

### Annotating Email Address Tokens
- [func annotateAddressesForSession(MEComposeSession, completion: ([MEEmailAddress : MEAddressAnnotation]) -> Void)](./mecomposesessionhandler/annotateaddressesforsession%28_,completion%29.md)
  Indicates whether recipients in the compose window are valid or not.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mailkit/meaddressannotation)*