# startSearchingForNewAccessories()

**Framework**: HomeKit  
**Kind**: method  
**Role**: Instance Method

Starts searching for accessories not yet associated with a home.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- visionOS 1.0+

## Declaration

```swift
func startSearchingForNewAccessories()
```

```objc
- (void) startSearchingForNewAccessories;
```

#### Discussion

HomeKit notifies your accessory browser delegate by calling the [`accessoryBrowser(_:didFindNewAccessory:)`](../hmaccessorybrowserdelegate/accessorybrowser%28_,didfindnewaccessory%29.md) and [`accessoryBrowser(_:didRemoveNewAccessory:)`](../hmaccessorybrowserdelegate/accessorybrowser%28_,didremovenewaccessory%29.md) methods when it detects accessories being added or removed, respectively.

When you start a search, HomeKit clears the [`discoveredAccessories`](./discoveredaccessories.md) array of content from the previous search.

## See Also

### Discovering accessories
- [var discoveredAccessories: [HMAccessory]](./discoveredaccessories.md)
  An array of accessories discovered during a search.
- [func stopSearchingForNewAccessories()](./stopsearchingfornewaccessories%28%29.md)
  Stops searching for new accessories.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmaccessorybrowser/startsearchingfornewaccessories())*