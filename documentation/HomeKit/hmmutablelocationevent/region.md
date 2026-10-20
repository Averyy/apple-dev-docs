# region

**Framework**: HomeKit  
**Kind**: property  
**Role**: Instance Property

The region on which events are triggered.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 11.0+
- tvOS 11.0+
- watchOS 4.0+

## Declaration

```swift
var region: CLRegion? { get set }
```

```objc
@property (nonatomic, strong, readwrite, nullable) CLRegion * region;
```

#### Discussion

Use this property to set the region on which the location event is triggered. The region object must have at least one of [`notifyOnEntry`](../../CoreLocation/clregion/notifyonentry.md) or [`notifyOnExit`](../../CoreLocation/clregion/notifyonexit.md) set to [`true`](../../Swift/true.md).

This property is `nil` when an application is not authorized for location services.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmmutablelocationevent/region)*