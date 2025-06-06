# removeZone(_:completionHandler:)

**Framework**: HomeKit  
**Kind**: method

Removes a zone from the home.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 14.0+
- visionOS 1.0+

## Declaration

```swift
func removeZone(_ zone: HMZone) async throws
```

## Parameters

- `zone`: The zone to remove.
- `completion`: The block executed after the request is processed.

## See Also

- [var zones: [HMZone]](hmhome/zones.md)
  An array of all the zones in the home.
- [func addZone(withName: String, completionHandler: (HMZone?, (any Error)?) -> Void)](hmhome/addzone(withname:completionhandler:).md)
  Adds a new zone to the home.
- [class HMZone](hmzone.md)
  A collection of rooms that users think of as a single area, like upstairs or downstairs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmhome/removezone(_:completionhandler:))*