# init(placemark:event:)

**Framework**: Intents  
**Kind**: init  
**Role**: Initializer

Initializes the event trigger with the specified location-based information.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
init(placemark: CLPlacemark, event: INSpatialEvent)
```

```objc
- (instancetype) initWithPlacemark:(CLPlacemark *) placemark event:(INSpatialEvent) event;
```

## Return Value

An initialized event trigger object or `nil` if the object could not be created.

## Parameters

- `placemark`: The location for which events are triggered.
- `event`: A constant indicating whether events are delivered when arriving or leaving the specified location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inspatialeventtrigger/init(placemark:event:))*