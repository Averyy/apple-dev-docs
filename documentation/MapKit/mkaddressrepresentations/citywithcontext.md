# cityWithContext(_:)

**Framework**: MapKit  
**Kind**: method

The city name and, optionally and if applicable, state and region to provide additional disambiguating context.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

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