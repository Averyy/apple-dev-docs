# addZone(withName:completionHandler:)

**Framework**: HomeKit  
**Kind**: method

Adds a new zone to the home.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 14.0+
- visionOS 1.0+

## Declaration

```swift
func addZone(named zoneName: String) async throws -> HMZone
```

## Parameters

- `zoneName`: The name of the new zone. Must not be  , and must not be the name of a zone already in the home.
- `completion`: The block executed after the request is processed.

## See Also

- [var zones: [HMZone]](hmhome/zones.md)
  An array of all the zones in the home.
- [func removeZone(HMZone, completionHandler: ((any Error)?) -> Void)](hmhome/removezone(_:completionhandler:).md)
  Removes a zone from the home.
- [class HMZone](hmzone.md)
  A collection of rooms that users think of as a single area, like upstairs or downstairs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmhome/addzone(withname:completionhandler:))*