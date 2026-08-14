# ABCreateStringWithAddressDictionary(_:_:)

**Framework**: Address Book UI  
**Kind**: func

Returns a formatted address from an address property.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+

## Declaration

```swift
func ABCreateStringWithAddressDictionary(_ address: [AnyHashable : Any], _ addCountryName: Bool) -> String
```

#### Return Value

The formatted address (may include line endings).

#### Discussion

The address is formatted based on the address’s country code ([`kABPersonAddressCountryCodeKey`](https://developer.apple.com/documentation/addressbook/kabpersonaddresscountrycodekey)).  In general, the country code should be set to correspond with the country or region name ([`kABPersonAddressCountryKey`](https://developer.apple.com/documentation/addressbook/kabpersonaddresscountrykey)).

## Parameters

- `address`: A dictionary representing the address property to format.
- `addCountryName`: Specifies whether to include the name of the country or region in the returned formatted address. When [`false`](https://developer.apple.com/documentation/swift/false) and address includes a country or region name, that country or region name is still included in the return value. When [`true`](https://developer.apple.com/documentation/swift/true) and `address` doesn’t include a country or region name, the country or region name is added to the return value. (The country or region name is generated from the country code entry in `address`; see `Address Property`.)

## See Also

- [class ABNewPersonViewController](abnewpersonviewcontroller.md)
  A view controller presenting an interface to create a contact.
- [class ABPersonViewController](abpersonviewcontroller.md)
  The `ABPersonViewController` class (whose instances are known as **person view controllers**) implements the view used to display a person record (`ABPersonRef`).
- [class ABUnknownPersonViewController](abunknownpersonviewcontroller.md)
  The `ABUnknownPersonViewController` class (whose instances are known as **unknown-person view controllers**) implements a view controller used to create a person record from a set of person properties.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbookui/abcreatestringwithaddressdictionary(_:_:))*