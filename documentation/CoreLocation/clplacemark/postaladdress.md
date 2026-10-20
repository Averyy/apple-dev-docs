# postalAddress

**Framework**: Core Location  
**Kind**: property  
**Role**: Instance Property

The postal address associated with the location, formatted for use with the Contacts framework.

**Availability**:
- iOS 11.0+ - Deprecated in 27.2
- iPadOS 11.0+ - Deprecated in 27.2
- Mac Catalyst 13.1+ - Deprecated in 27.0
- macOS 10.13+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2
- watchOS 4.0+ - Deprecated in 27.2

> **Deprecated**: Use either GeoToolbox.PlaceDescriptor or MapKit

## Declaration

```swift
var postalAddress: CNPostalAddress? { get }
```

```objc
@property (nonatomic, readonly, nullable) CNPostalAddress * postalAddress;
```

## See Also

### Getting the associated contact details
- [var addressDictionary: [AnyHashable : Any]?](./addressdictionary.md)
  A dictionary containing the Address Book keys and values for the placemark.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/clplacemark/postaladdress)*