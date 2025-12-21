# CNPostalAddress

**Framework**: Contacts  
**Kind**: class

An immutable representation of the postal address for a contact.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class CNPostalAddress
```

#### Overview

`CNPostalAddress` is a thread-safe class.

## Topics

### Getting the Parts of a Postal Address
- [var street: String](cnpostaladdress/street.md)
  The street name in a postal address.
- [var city: String](cnpostaladdress/city.md)
  The city name in a postal address.
- [var state: String](cnpostaladdress/state.md)
  The state name in a postal address.
- [var postalCode: String](cnpostaladdress/postalcode.md)
  The postal code in a postal address.
- [var country: String](cnpostaladdress/country.md)
  The country or region name in a postal address.
- [var isoCountryCode: String](cnpostaladdress/isocountrycode.md)
  The ISO country code for the country or region in a postal address, using the ISO 3166-1 alpha-2 standard.
- [var subAdministrativeArea: String](cnpostaladdress/subadministrativearea.md)
  The subadministrative area (such as a county or other region) in a postal address.
- [var subLocality: String](cnpostaladdress/sublocality.md)
  Additional information associated with the location, typically defined at the city or town level, in a postal address.
### Getting Localized Postal Values
- [class func localizedString(forKey: String) -> String](cnpostaladdress/localizedstring(forkey:).md)
  Returns the localized name for the property associated with the specified key.
- [let CNPostalAddressStreetKey: String](cnpostaladdressstreetkey.md)
  The street name of the address.
- [let CNPostalAddressCityKey: String](cnpostaladdresscitykey.md)
  The city of the address.
- [let CNPostalAddressStateKey: String](cnpostaladdressstatekey.md)
  The state name of the address.
- [let CNPostalAddressPostalCodeKey: String](cnpostaladdresspostalcodekey.md)
  The postal code of the address.
- [let CNPostalAddressCountryKey: String](cnpostaladdresscountrykey.md)
  The country or region name of the address.
- [let CNPostalAddressISOCountryCodeKey: String](cnpostaladdressisocountrycodekey.md)
  The ISO country code of the address.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [CNMutablePostalAddress](cnmutablepostaladdress.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSMutableCopying](../Foundation/NSMutableCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class CNMutablePostalAddress](cnmutablepostaladdress.md)
  A mutable representation of the postal address for a contact.
- [class CNInstantMessageAddress](cninstantmessageaddress.md)
  An immutable object representing an instant message address for the contact.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contacts/cnpostaladdress)*