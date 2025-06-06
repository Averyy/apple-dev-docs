# removeHome(_:completionHandler:)

**Framework**: HomeKit  
**Kind**: method

Removes a home from this home manager.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- visionOS 1.0+

## Declaration

```swift
func removeHome(_ home: HMHome) async throws
```

#### Discussion

This method returns an error if the specified home is not managed by the home manager.

## Parameters

- `home`: The home to remove.
- `completion`: The block executed after the request is processed.

## See Also

- [func addHome(withName: String, completionHandler: (HMHome?, (any Error)?) -> Void)](hmhomemanager/addhome(withname:completionhandler:).md)
  Adds a new home to this home manager.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmhomemanager/removehome(_:completionhandler:))*