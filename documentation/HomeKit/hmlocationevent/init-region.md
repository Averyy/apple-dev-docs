# init(region:)

**Framework**: HomeKit  
**Kind**: init

Creates a new location event with the specified region.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 9.0+

## Declaration

```swift
init(region: CLRegion)
```

#### Return Value

An initialized instance representing the location event.

## Parameters

- `region`: Region on which the event is triggered. The region object must have at least one of [`notifyOnEntry`](https://developer.apple.com/documentation/corelocation/clregion/notifyonentry) or [`notifyOnExit`](https://developer.apple.com/documentation/corelocation/clregion/notifyonexit) set to [`true`](https://developer.apple.com/documentation/swift/true).


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmlocationevent/init(region:))*