# home(_:didUnblockAccessory:)

**Framework**: HomeKit  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (void) home:(HMHome *) home didUnblockAccessory:(HMAccessory *) accessory;
```

## Parameters

- `home`: The home.
- `accessory`: The accessory that was unblocked.

## See Also

### Observing Accessories
- [func home(HMHome, didEncounterError: any Error, for: HMAccessory)](./home%28_,didencountererror,for%29.md)
  Tells the delegate that a configured accessory encountered an error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmhomedelegate/home(_:didunblockaccessory:))*