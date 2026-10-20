# addZone(withName:completionHandler:)

**Framework**: HomeKit  
**Kind**: method  
**Role**: Instance Method

Adds a new zone to the home.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 14.0+
- visionOS 1.0+

## Declaration

```swift
func addZone(withName zoneName: String, completionHandler completion: @escaping @Sendable (HMZone?, (any Error)?) -> Void)
```

```swift
func addZone(named zoneName: String) async throws -> HMZone
```

```objc
- (void) addZoneWithName:(NSString *) zoneName completionHandler:(void (^)(HMZone *zone, NSError *error)) completion;
```

## Parameters

- `zoneName`: The name of the new zone. Must not be `nil`, and must not be the name of a zone already in the home.
- `completion`: The block executed after the request is processed.

  - **zone**: The newly created zone.
  - **error**: `nil` on success; otherwise, error object indicating the reason for failure.

## See Also

### Grouping rooms into zones
- [var zones: [HMZone]](./zones.md)
  An array of all the zones in the home.
- [func removeZone(HMZone, completionHandler: ((any Error)?) -> Void)](./removezone%28_,completionhandler%29.md)
  Removes a zone from the home.
- [class HMZone](../hmzone.md)
  A collection of rooms that users think of as a single area, like upstairs or downstairs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmhome/addzone(withname:completionhandler:))*