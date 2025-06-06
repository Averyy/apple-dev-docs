# isoCountryCode

**Framework**: Core Location  
**Kind**: property

The abbreviated country or region name.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var isoCountryCode: String? { get }
```

#### Discussion

This string is the standard abbreviation used to refer to the country or region. For example, if the placemark location is Apple’s headquarters, the value for this property would be the string “US”.

## See Also

- [var country: String?](clplacemark/country.md)
  The name of the country or region associated with the placemark.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/clplacemark/isocountrycode)*