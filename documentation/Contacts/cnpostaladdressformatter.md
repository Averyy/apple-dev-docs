# CNPostalAddressFormatter

**Framework**: Contacts  
**Kind**: class

An object that you use to format a contact’s postal addresses.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class CNPostalAddressFormatter
```

#### Overview

A `CNPostalAddressFormatter` object handles international formatting of postal addresses. It is recommended that you create an instance of this class when formatting many postal addresses, and use the instance methods; otherwise use the class methods.

## Topics

### Generating a formatted attributed string
- [func attributedString(from: CNPostalAddress, withDefaultAttributes: [AnyHashable : Any]) -> NSAttributedString](cnpostaladdressformatter/attributedstring(from:withdefaultattributes:).md)
  Returns a formatted postal address as an attributed string.
- [class func attributedString(from: CNPostalAddress, style: CNPostalAddressFormatterStyle, withDefaultAttributes: [AnyHashable : Any]) -> NSAttributedString](cnpostaladdressformatter/attributedstring(from:style:withdefaultattributes:).md)
  Returns a postal address as an attributed string and formatted for the specified style.
- [let CNPostalAddressPropertyAttribute: String](cnpostaladdresspropertyattribute.md)
  An attribute that identifies the purpose of a range of characters in an attributed string.
- [let CNPostalAddressLocalizedPropertyNameAttribute: String](cnpostaladdresslocalizedpropertynameattribute.md)
  An attribute that identifies the localized property of postal address.
### Generating a formatted string
- [func string(from: CNPostalAddress) -> String](cnpostaladdressformatter/string(from:).md)
  Returns a formatted postal address.
- [class func string(from: CNPostalAddress, style: CNPostalAddressFormatterStyle) -> String](cnpostaladdressformatter/string(from:style:).md)
  Returns a postal address as a string and formatted for the specified style.
### Specifying the formatting style
- [var style: CNPostalAddressFormatterStyle](cnpostaladdressformatter/style.md)
  The style to apply when formatting strings.
- [enum CNPostalAddressFormatterStyle](cnpostaladdressformatterstyle.md)
  Constants for postal formatting styles.
### Getting the postal attribute keys
- [let CNPostalAddressCityKey: String](cnpostaladdresscitykey.md)
  The city of the address.
- [let CNPostalAddressCountryKey: String](cnpostaladdresscountrykey.md)
  The country or region name of the address.
- [let CNPostalAddressISOCountryCodeKey: String](cnpostaladdressisocountrycodekey.md)
  The ISO country code of the address.
- [let CNPostalAddressPostalCodeKey: String](cnpostaladdresspostalcodekey.md)
  The postal code of the address.
- [let CNPostalAddressStateKey: String](cnpostaladdressstatekey.md)
  The state name of the address.
- [let CNPostalAddressStreetKey: String](cnpostaladdressstreetkey.md)
  The street name of the address.
- [let CNPostalAddressSubAdministrativeAreaKey: String](cnpostaladdresssubadministrativeareakey.md)
  The subadministrative area of the address.
- [let CNPostalAddressSubLocalityKey: String](cnpostaladdresssublocalitykey.md)
  The sublocality of the address.

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

## See Also

- [class CNContactFormatter](cncontactformatter.md)
  An object that you use to format contact information before displaying it to the user.
- [class CNContactVCardSerialization](cncontactvcardserialization.md)
  An object you use to convert to and from a vCard representation of the user’s contacts.
- [class CNContactsUserDefaults](cncontactsuserdefaults.md)
  An object that defines the default options to use when displaying contacts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contacts/cnpostaladdressformatter)*