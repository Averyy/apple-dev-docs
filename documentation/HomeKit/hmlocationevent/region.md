# region

**Framework**: HomeKit  
**Kind**: property

The region on which events are triggered.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 9.0+
- tvOS 10.0+
- watchOS 2.0+

## Declaration

```swift
var region: CLRegion? { get }
```

#### Discussion

The event is triggered based on the values of the [`notifyOnEntry`](https://developer.apple.com/documentation/CoreLocation/CLRegion/notifyOnEntry) and [`notifyOnExit`](https://developer.apple.com/documentation/CoreLocation/CLRegion/notifyOnExit) properties.

This property is `nil` when an application is not authorized for location services.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmlocationevent/region)*