# city

**Framework**: Contacts  
**Kind**: property  
**Role**: Instance Property

The city name in a postal address.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var city: String { get }
```

*iOS, iPadOS, Mac Catalyst, visionOS, watchOS*

```objc
@property (nonatomic, copy, readonly) NSString * city;
```

*macOS*

```objc
@property (atomic, copy, readonly) NSString * city;
```

## See Also

### Getting the Parts of a Postal Address
- [var street: String](./street.md)
  The street name in a postal address.
- [var state: String](./state.md)
  The state name in a postal address.
- [var postalCode: String](./postalcode.md)
  The postal code in a postal address.
- [var country: String](./country.md)
  The country or region name in a postal address.
- [var isoCountryCode: String](./isocountrycode.md)
  The ISO country code for the country or region in a postal address, using the ISO 3166-1 alpha-2 standard.
- [var subAdministrativeArea: String](./subadministrativearea.md)
  The subadministrative area (such as a county or other region) in a postal address.
- [var subLocality: String](./sublocality.md)
  Additional information associated with the location, typically defined at the city or town level, in a postal address.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contacts/cnpostaladdress/city)*