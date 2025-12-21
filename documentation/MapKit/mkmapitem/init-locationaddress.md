# init(location:address:)

**Framework**: MapKit  
**Kind**: init

Creates and returns a map item object using the specified location and address objects.

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
init(location: CLLocation, address: MKAddress?)
```

#### Return Value

An initialized map item object.

#### Discussion

Use this method to create a map item for a specific location. Don’t use it to create a map item representing the current location of someone’s device, instead use the ```MKMapItem/forCurrentLocation()`` method.

## Parameters

- `location`: A  .
- `address`: An  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmapitem/init(location:address:))*