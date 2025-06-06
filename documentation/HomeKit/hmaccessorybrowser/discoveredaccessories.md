# discoveredAccessories

**Framework**: HomeKit  
**Kind**: property

An array of accessories discovered during a search.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- visionOS 1.0+

## Declaration

```swift
var discoveredAccessories: [HMAccessory] { get }
```

#### Discussion

When you start a new search by calling the [`startSearchingForNewAccessories()`](hmaccessorybrowser/startsearchingfornewaccessories().md) method, HomeKit clears the [`discoveredAccessories`](hmaccessorybrowser/discoveredaccessories.md) array. It then modifies the array as it discovers new accessories until you end the search by calling the [`stopSearchingForNewAccessories()`](hmaccessorybrowser/stopsearchingfornewaccessories().md) method.

## See Also

- [func startSearchingForNewAccessories()](hmaccessorybrowser/startsearchingfornewaccessories.md)
  Starts searching for accessories not yet associated with a home.
- [func stopSearchingForNewAccessories()](hmaccessorybrowser/stopsearchingfornewaccessories.md)
  Stops searching for new accessories.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmaccessorybrowser/discoveredaccessories)*