# init(region:)

**Framework**: HomeKit  
**Kind**: init  
**Role**: Initializer

Creates a new location event with the specified region.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 9.0+

## Declaration

```swift
init(region: CLRegion)
```

```objc
- (instancetype) initWithRegion:(CLRegion *) region;
```

#### Return Value

An initialized instance representing the location event.

## Parameters

- `region`: Region on which the event is triggered. The region object must have at least one of [`notifyOnEntry`](../../CoreLocation/clregion/notifyonentry.md) or [`notifyOnExit`](../../CoreLocation/clregion/notifyonexit.md) set to [`true`](../../Swift/true.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmlocationevent/init(region:))*