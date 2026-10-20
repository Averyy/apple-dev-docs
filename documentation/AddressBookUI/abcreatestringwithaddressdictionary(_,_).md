# ABCreateStringWithAddressDictionary(_:_:)

**Framework**: Address Book UI  
**Kind**: func  
**Role**: Function

Returns a formatted address from an address property.

**Availability**:
- iOS 2.0+ - Deprecated in 9.0
- iPadOS 2.0+ - Deprecated in 9.0
- Mac Catalyst 13.1+ - Deprecated in 13.1

> **Deprecated**: Use [`CNPostalAddressFormatter`](../Contacts/cnpostaladdressformatter.md) instead.

## Declaration

```swift
func ABCreateStringWithAddressDictionary(_ address: [AnyHashable : Any], _ addCountryName: Bool) -> String
```

```c
NSString *ABCreateStringWithAddressDictionary(NSDictionary *address, BOOL addCountryName);
```

#### Return Value

The formatted address (may include line endings).

#### Discussion

The address is formatted based on the address’s country code ([`kABPersonAddressCountryCodeKey`](../AddressBook/kabpersonaddresscountrycodekey.md)).  In general, the country code should be set to correspond with the country or region name ([`kABPersonAddressCountryKey`](../AddressBook/kabpersonaddresscountrykey.md)).

## Parameters

- `address`: A dictionary representing the address property to format.
- `addCountryName`: Specifies whether to include the name of the country or region in the returned formatted address.

  When [`false`](../Swift/false.md) and address includes a country or region name, that country or region name is still included in the return value.

  When [`true`](../Swift/true.md) and `address` doesn’t include a country or region name, the country or region name is added to the return value. (The country or region name is generated from the country code entry in `address`; see `Address Property`.)

## See Also

### Detail Display
- [class ABNewPersonViewController](./abnewpersonviewcontroller.md)
  A view controller presenting an interface to create a contact.
- [class ABPersonViewController](./abpersonviewcontroller.md)
  The `ABPersonViewController` class (whose instances are known as **person view controllers**) implements the view used to display a person record (`ABPersonRef`).
- [class ABUnknownPersonViewController](./abunknownpersonviewcontroller.md)
  The `ABUnknownPersonViewController` class (whose instances are known as **unknown-person view controllers**) implements a view controller used to create a person record from a set of person properties.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbookui/abcreatestringwithaddressdictionary(_:_:))*