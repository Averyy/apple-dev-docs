# subLocality

**Framework**: Contacts  
**Kind**: property  
**Role**: Instance Property

Additional information associated with the location, typically defined at the city or town level, in a postal address.

**Availability**:
- iOS 10.3+
- iPadOS 10.3+
- Mac Catalyst 13.1+
- macOS 10.12.4+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
var subLocality: String { get set }
```

*iOS, iPadOS, Mac Catalyst, visionOS, watchOS*

```objc
@property (nonatomic, copy) NSString * subLocality;
```

*macOS*

```objc
@property (atomic, copy) NSString * subLocality;
```

## See Also

### Modifying the Parts of a Postal Address
- [var street: String](./street.md)
  The street name of the address.
- [var city: String](./city.md)
  The city name of the address.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/contacts/cnmutablepostaladdress/sublocality)*