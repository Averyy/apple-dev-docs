# region

**Framework**: HomeKit  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic, strong, readonly, nullable) CLRegion * region;
```

## Discussion

The event is triggered based on the values of the [`notifyOnEntry`](../../CoreLocation/clregion/notifyonentry.md) and [`notifyOnExit`](../../CoreLocation/clregion/notifyonexit.md) properties.

This property is `nil` when an application is not authorized for location services.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmlocationevent/region)*