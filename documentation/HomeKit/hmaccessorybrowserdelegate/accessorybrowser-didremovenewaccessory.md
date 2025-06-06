# accessoryBrowser(_:didRemoveNewAccessory:)

**Framework**: HomeKit  
**Kind**: method

Tells the delegate that a new accessory is no longer available in the browser.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- visionOS 1.0+

## Declaration

```swift
optional func accessoryBrowser(_ browser: HMAccessoryBrowser, didRemoveNewAccessory accessory: HMAccessory)
```

#### Discussion

A common reason for an accessory to no longer be available is because it was added to a home, and is thus no longer a new accessory.

## Parameters

- `browser`: The browser.
- `accessory`: The accessory that is no longer available.

## See Also

- [func accessoryBrowser(HMAccessoryBrowser, didFindNewAccessory: HMAccessory)](hmaccessorybrowserdelegate/accessorybrowser(_:didfindnewaccessory:).md)
  Tells the delegate that a new accessory has been discovered.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmaccessorybrowserdelegate/accessorybrowser(_:didremovenewaccessory:))*