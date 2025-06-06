# CNContactFormatter

**Framework**: Contacts  
**Kind**: class

An object that you use to format contact information before displaying it to the user.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class CNContactFormatter
```

#### Overview

A `CNContactFormatter` object handles international ordering and delimiting for the contact name components. When formatting many contacts, create an instance of this class and use the instance methods; otherwise use the class methods.

## Topics

### Creating a formatted attributed string
- [func attributedString(from: CNContact, defaultAttributes: [AnyHashable : Any]?) -> NSAttributedString?](cncontactformatter/attributedstring(from:defaultattributes:).md)
  Formats the contact name as an attributed string.
- [class func attributedString(from: CNContact, style: CNContactFormatterStyle, defaultAttributes: [AnyHashable : Any]?) -> NSAttributedString?](cncontactformatter/attributedstring(from:style:defaultattributes:).md)
  Formats the contact name as an attributed string.
### Creating a formatted string
- [func string(from: CNContact) -> String?](cncontactformatter/string(from:).md)
  Formats the contact name.
- [class func string(from: CNContact, style: CNContactFormatterStyle) -> String?](cncontactformatter/string(from:style:).md)
  Returns the contact name, formatted with the specified formatter.
### Specifying the formatting style
- [var style: CNContactFormatterStyle](cncontactformatter/style.md)
  The formatting style for the contact name.
- [enum CNContactFormatterStyle](cncontactformatterstyle.md)
  The formatting styles for contact names.
### Getting a descriptor
- [class func descriptorForRequiredKeys(for: CNContactFormatterStyle) -> any CNKeyDescriptor](cncontactformatter/descriptorforrequiredkeys(for:).md)
  Returns the required key descriptor for the specified formatting style of the contact.
- [class var descriptorForRequiredKeysForDelimiter: any CNKeyDescriptor](cncontactformatter/descriptorforrequiredkeysfordelimiter.md)
  Returns the required key descriptor for the name delimiter.
- [class var descriptorForRequiredKeysForNameOrder: any CNKeyDescriptor](cncontactformatter/descriptorforrequiredkeysfornameorder.md)
  Returns the required key descriptor for the display name order.
### Getting format information
- [class func delimiter(for: CNContact) -> String](cncontactformatter/delimiter(for:).md)
  Returns the delimiter to use between name components.
- [class func nameOrder(for: CNContact) -> CNContactDisplayNameOrder](cncontactformatter/nameorder(for:).md)
  Returns the display name order.
- [enum CNContactDisplayNameOrder](cncontactdisplaynameorder.md)
  The formatting orders for contact names component.

## Relationships

### Inherits From
- [Formatter](../Foundation/Formatter.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)

## See Also

- [class CNPostalAddressFormatter](cnpostaladdressformatter.md)
  An object that you use to format a contact’s postal addresses.
- [class CNContactVCardSerialization](cncontactvcardserialization.md)
  An object you use to convert to and from a vCard representation of the user’s contacts.
- [class CNContactsUserDefaults](cncontactsuserdefaults.md)
  An object that defines the default options to use when displaying contacts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contacts/cncontactformatter)*