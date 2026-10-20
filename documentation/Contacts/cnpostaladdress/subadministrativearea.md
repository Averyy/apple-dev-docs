# subAdministrativeArea

**Framework**: Contacts  
**Kind**: property  
**Role**: Instance Property

The subadministrative area (such as a county or other region) in a postal address.

**Availability**:
- iOS 10.3+
- iPadOS 10.3+
- Mac Catalyst 13.1+
- macOS 10.12.4+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
var subAdministrativeArea: String { get }
```

*iOS, iPadOS, Mac Catalyst, visionOS, watchOS*

```objc
@property (nonatomic, copy, readonly) NSString * subAdministrativeArea;
```

*macOS*

```objc
@property (atomic, copy, readonly) NSString * subAdministrativeArea;
```

## See Also

### Getting the Parts of a Postal Address
- [var street: String](./street.md)
  The street name in a postal address.
- [var city: String](./city.md)
  The city name in a postal address.
- [var state: String](./state.md)
  The state name in a postal address.
- [var postalCode: String](./postalcode.md)
  The postal code in a postal address.
- [var country: String](./country.md)
  The country or region name in a postal address.
- [var isoCountryCode: String](./isocountrycode.md)
  The ISO country code for the country or region in a postal address, using the ISO 3166-1 alpha-2 standard.
- [var subLocality: String](./sublocality.md)
  Additional information associated with the location, typically defined at the city or town level, in a postal address.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contacts/cnpostaladdress/subadministrativearea)*