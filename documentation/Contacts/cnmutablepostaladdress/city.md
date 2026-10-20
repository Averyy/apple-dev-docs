# city

**Framework**: Contacts  
**Kind**: property  
**Role**: Instance Property

The city name of the address.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var city: String { get set }
```

*iOS, iPadOS, Mac Catalyst, visionOS, watchOS*

```objc
@property (nonatomic, copy) NSString * city;
```

*macOS*

```objc
@property (atomic, copy) NSString * city;
```

## See Also

### Modifying the Parts of a Postal Address
- [var street: String](./street.md)
  The street name of the address.
- [var state: String](./state.md)
  The state name of the address.
- [var postalCode: String](./postalcode.md)
  The postal code of the address.
- [var country: String](./country.md)
  The country or region name of the address.
- [var isoCountryCode: String](./isocountrycode.md)
  The ISO country code, using the ISO 3166-1 alpha-2 standard.
- [var subAdministrativeArea: String](./subadministrativearea.md)
  The subadministrative area (such as a county or other region) in a postal address.
- [var subLocality: String](./sublocality.md)
  Additional information associated with the location, typically defined at the city or town level, in a postal address.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contacts/cnmutablepostaladdress/city)*