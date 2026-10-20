# accessoryBrowser(_:didFindNewAccessory:)

**Framework**: HomeKit  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that a new accessory has been discovered.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- visionOS 1.0+

## Declaration

```swift
optional func accessoryBrowser(_ browser: HMAccessoryBrowser, didFindNewAccessory accessory: HMAccessory)
```

```objc
- (void) accessoryBrowser:(HMAccessoryBrowser *) browser didFindNewAccessory:(HMAccessory *) accessory;
```

## Parameters

- `browser`: The browser that discovered the new accessory.
- `accessory`: The new accessory.

## See Also

### Tracking new accessories
- [func accessoryBrowser(HMAccessoryBrowser, didRemoveNewAccessory: HMAccessory)](./accessorybrowser%28_,didremovenewaccessory%29.md)
  Tells the delegate that a new accessory is no longer available in the browser.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmaccessorybrowserdelegate/accessorybrowser(_:didfindnewaccessory:))*