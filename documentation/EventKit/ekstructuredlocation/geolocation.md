# geoLocation

**Framework**: EventKit  
**Kind**: property  
**Role**: Instance Property

The core location.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var geoLocation: CLLocation? { get set }
```

```objc
@property (nonatomic, strong, nullable) CLLocation * geoLocation;
```

## Mentions

- [Setting an alarm](../setting-an-alarm.md)

## See Also

### Accessing Structured Location Properties
- [var title: String?](./title.md)
  The title of the location.
- [var radius: Double](./radius.md)
  A minimum distance from the core location that would trigger the alarm or reminder.


---

*[View on Apple Developer](https://developer.apple.com/documentation/eventkit/ekstructuredlocation/geolocation)*