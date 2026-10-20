# fullAddress(includingRegion:singleLine:)

**Framework**: MapKit  
**Kind**: method

Returns the the location’s full address, optionally including the country or on a single link without line breaks.

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
func fullAddress(includingRegion: Bool, singleLine: Bool) -> String?
```

## Parameters

- `includingRegion`: A Boolean value that indicates whether the address should include the region name.
- `singleLine`: A Boolean value that indicates whether the framework should format the address as a single line.

## See Also

- [func cityWithContext(MKAddressRepresentations.ContextStyle) -> String?](mkaddressrepresentations/citywithcontext(_:).md)
  The city name and, optionally and if applicable, state and region to provide additional disambiguating context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkaddressrepresentations/fulladdress(includingregion:singleline:))*