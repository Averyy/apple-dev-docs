# PlaceDescriptor.SupportingPlaceRepresentation.serviceIdentifiers(_:)

**Framework**: GeoToolbox  
**Kind**: case

Identifiers that represent a place for different mapping service providers

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
case serviceIdentifiers([String : String])
```

#### Discussion

A service identifier is a [`Dictionary`](https://developer.apple.com/documentation/Swift/Dictionary) that maps a bundle IDs (key) and a unique identifiers (value) that represent a mapping between a specific service provider and their specific identifier for a place. For example, the dictionary entry `[com.apple.maps: IBE1F65094A7A13B1]` maps a service provider to a unique ID — here `com.apple.maps`, which represents Apple Maps, and the place ID, `IBE1F65094A7A13B1`, a string that represents the San Francisco Ferry Building, in San Francisco, California.

You can use Apple Maps service identifiers, or those from other mapping services to enable GeoToolbox to attempt to resolve rich data for the specified place or a specified use case, such as a street address, or the coordinate of a physical location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/geotoolbox/placedescriptor/supportingplacerepresentation/serviceidentifiers(_:))*