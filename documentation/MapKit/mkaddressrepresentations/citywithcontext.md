# cityWithContext(_:)

**Framework**: MapKit  
**Kind**: method

The city name and, optionally and if applicable, state and region to provide additional disambiguating context.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
func cityWithContext(_ style: MKAddressRepresentations.ContextStyle) -> String?
```

## Parameters

- `style`: The   to apply.

## See Also

- [func fullAddress(includingRegion: Bool, singleLine: Bool) -> String?](mkaddressrepresentations/fulladdress(includingregion:singleline:).md)
  Returns the the location’s full address, optionally including the country or on a single link without line breaks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkaddressrepresentations/citywithcontext(_:))*