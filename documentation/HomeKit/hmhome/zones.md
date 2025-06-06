# zones

**Framework**: HomeKit  
**Kind**: property

An array of all the zones in the home.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 14.0+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var zones: [HMZone] { get }
```

## See Also

- [func addZone(withName: String, completionHandler: (HMZone?, (any Error)?) -> Void)](hmhome/addzone(withname:completionhandler:).md)
  Adds a new zone to the home.
- [func removeZone(HMZone, completionHandler: ((any Error)?) -> Void)](hmhome/removezone(_:completionhandler:).md)
  Removes a zone from the home.
- [class HMZone](hmzone.md)
  A collection of rooms that users think of as a single area, like upstairs or downstairs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmhome/zones)*