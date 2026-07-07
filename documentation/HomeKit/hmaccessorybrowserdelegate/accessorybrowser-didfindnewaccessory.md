# accessoryBrowser(_:didFindNewAccessory:)

**Framework**: HomeKit  
**Kind**: method

Tells the delegate that a new accessory has been discovered.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- visionOS 1.0+

## Declaration

```swift
optional func accessoryBrowser(_ browser: HMAccessoryBrowser, didFindNewAccessory accessory: HMAccessory)
```

## Parameters

- `browser`: The browser that discovered the new accessory.
- `accessory`: The new accessory.

## See Also

- [func accessoryBrowser(HMAccessoryBrowser, didRemoveNewAccessory: HMAccessory)](hmaccessorybrowserdelegate/accessorybrowser(_:didremovenewaccessory:).md)
  Tells the delegate that a new accessory is no longer available in the browser.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmaccessorybrowserdelegate/accessorybrowser(_:didfindnewaccessory:))*