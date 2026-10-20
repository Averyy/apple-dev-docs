# cityWithContext(_:)

**Framework**: MapKit  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (NSString *) cityWithContextUsingStyle:(MKAddressRepresentationsContextStyle) style;
```

## Parameters

- `style`: The [`MKAddressRepresentations.ContextStyle`](./contextstyle.md) to apply.

## See Also

### Getting a full address and city name
- [func fullAddress(includingRegion: Bool, singleLine: Bool) -> String?](./fulladdress%28includingregion,singleline%29.md)
  Returns the the location’s full address, optionally including the country or on a single link without line breaks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkaddressrepresentations/citywithcontext(_:))*