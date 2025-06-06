# home(_:didEncounterError:for:)

**Framework**: HomeKit  
**Kind**: method

Tells the delegate that a configured accessory encountered an error.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
optional func home(_ home: HMHome, didEncounterError error: any Error, for accessory: HMAccessory)
```

#### Discussion

The delegate should check whether the accessory is blocked.

## Parameters

- `home`: The home.
- `error`: The error encountered by the accessory.
- `accessory`: The accessory that encountered the error.

## See Also

- [func home(HMHome, didUnblockAccessory: HMAccessory)](hmhomedelegate/home(_:didunblockaccessory:).md)
  Tells the delegate that an accessory has been unblocked.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmhomedelegate/home(_:didencountererror:for:))*