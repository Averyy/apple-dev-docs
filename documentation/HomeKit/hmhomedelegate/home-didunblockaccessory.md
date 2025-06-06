# home(_:didUnblockAccessory:)

**Framework**: HomeKit  
**Kind**: method

Tells the delegate that an accessory has been unblocked.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
optional func home(_ home: HMHome, didUnblockAccessory accessory: HMAccessory)
```

## Parameters

- `home`: The home.
- `accessory`: The accessory that was unblocked.

## See Also

- [func home(HMHome, didEncounterError: any Error, for: HMAccessory)](hmhomedelegate/home(_:didencountererror:for:).md)
  Tells the delegate that a configured accessory encountered an error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmhomedelegate/home(_:didunblockaccessory:))*