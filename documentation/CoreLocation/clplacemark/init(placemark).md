# init(placemark:)

**Framework**: Core Location  
**Kind**: init  
**Role**: Initializer

Initializes and returns a placemark object from another placemark object.

**Availability**:
- iOS 5.0+ - Deprecated in 27.2
- iPadOS 5.0+ - Deprecated in 27.2
- Mac Catalyst 13.1+ - Deprecated in 27.0
- macOS 10.8+ - Deprecated in 27.2
- tvOS 9.0+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.2
- watchOS 2.0+ - Deprecated in 27.2

> **Deprecated**: Use either GeoToolbox.PlaceDescriptor or MapKit

## Declaration

```swift
init(placemark: CLPlacemark)
```

```objc
- (instancetype) initWithPlacemark:(CLPlacemark *) placemark;
```

#### Return Value

An initialized placemark object.

#### Discussion

You can use this method to transfer information from one placemark object to another placemark object.

## Parameters

- `placemark`: The placemark object to use as the source of the data for the new object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/clplacemark/init(placemark:))*