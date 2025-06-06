# stopSearchingForNewAccessories()

**Framework**: HomeKit  
**Kind**: method

Stops searching for new accessories.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- visionOS 1.0+

## Declaration

```swift
func stopSearchingForNewAccessories()
```

#### Discussion

After you call this method, HomeKit stops sending updates to your browser delegate. Scanning may continue for system reasons or if other delegates are still active, but the [`discoveredAccessories`](hmaccessorybrowser/discoveredaccessories.md) array remains unchanged after you stop the search until your app calls the [`startSearchingForNewAccessories()`](hmaccessorybrowser/startsearchingfornewaccessories().md) method again.

## See Also

- [var discoveredAccessories: [HMAccessory]](hmaccessorybrowser/discoveredaccessories.md)
  An array of accessories discovered during a search.
- [func startSearchingForNewAccessories()](hmaccessorybrowser/startsearchingfornewaccessories.md)
  Starts searching for accessories not yet associated with a home.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmaccessorybrowser/stopsearchingfornewaccessories())*