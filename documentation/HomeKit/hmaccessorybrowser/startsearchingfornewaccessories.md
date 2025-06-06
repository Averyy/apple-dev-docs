# startSearchingForNewAccessories()

**Framework**: HomeKit  
**Kind**: method

Starts searching for accessories not yet associated with a home.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- visionOS 1.0+

## Declaration

```swift
func startSearchingForNewAccessories()
```

#### Discussion

HomeKit notifies your accessory browser delegate by calling the [`accessoryBrowser(_:didFindNewAccessory:)`](hmaccessorybrowserdelegate/accessorybrowser(_:didfindnewaccessory:).md) and [`accessoryBrowser(_:didRemoveNewAccessory:)`](hmaccessorybrowserdelegate/accessorybrowser(_:didremovenewaccessory:).md) methods when it detects accessories being added or removed, respectively.

When you start a search, HomeKit clears the [`discoveredAccessories`](hmaccessorybrowser/discoveredaccessories.md) array of content from the previous search.

## See Also

- [var discoveredAccessories: [HMAccessory]](hmaccessorybrowser/discoveredaccessories.md)
  An array of accessories discovered during a search.
- [func stopSearchingForNewAccessories()](hmaccessorybrowser/stopsearchingfornewaccessories.md)
  Stops searching for new accessories.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmaccessorybrowser/startsearchingfornewaccessories())*