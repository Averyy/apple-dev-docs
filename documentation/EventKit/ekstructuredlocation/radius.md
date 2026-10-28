# radius

**Framework**: EventKit  
**Kind**: property  
**Role**: Instance Property

A minimum distance from the core location that would trigger the alarm or reminder.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var radius: Double { get set }
```

```objc
@property (nonatomic) double radius;
```

## Discussion

To use the default radius, set this property to `0`.

## See Also

### Accessing Structured Location Properties
- [var title: String?](./title.md)
  The title of the location.
- [var geoLocation: CLLocation?](./geolocation.md)
  The core location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/eventkit/ekstructuredlocation/radius)*