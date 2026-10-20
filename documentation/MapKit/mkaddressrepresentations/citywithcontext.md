# cityWithContext

**Framework**: MapKit  
**Kind**: property  
**Role**: Instance Property

The city name along with the country name, to provide additional disambiguating context.

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
var cityWithContext: String? { get }
```

```objc
@property (nonatomic, copy, readonly, nullable) NSString * cityWithContext;
```

#### Discussion

This returns the same value as `cityWithContext(.automatic)`.

## See Also

### Getting parts of an address
- [var cityName: String?](./cityname.md)
  The name of the city.
- [var regionName: String?](./regionname.md)
  The region name, such as “United States”.
- [var region: Locale.Region?](./region.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkaddressrepresentations/citywithcontext)*