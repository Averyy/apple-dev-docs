# addHome(withName:completionHandler:)

**Framework**: HomeKit  
**Kind**: method

Adds a new home to this home manager.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- visionOS 1.0+

## Declaration

```swift
func addHome(named homeName: String) async throws -> HMHome
```

## Parameters

- `homeName`: The name of the new home. Must not match the name of an existing home.
- `completion`: The block executed after the request is processed.

## See Also

- [func removeHome(HMHome, completionHandler: ((any Error)?) -> Void)](hmhomemanager/removehome(_:completionhandler:).md)
  Removes a home from this home manager.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmhomemanager/addhome(withname:completionhandler:))*