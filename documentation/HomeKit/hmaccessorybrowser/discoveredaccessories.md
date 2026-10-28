# discoveredAccessories

**Framework**: HomeKit  
**Kind**: property  
**Role**: Instance Property

An array of accessories discovered during a search.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- visionOS 1.0+

## Declaration

```swift
var discoveredAccessories: [HMAccessory] { get }
```

```objc
@property (nonatomic, copy, readonly) NSArray<HMAccessory *> * discoveredAccessories;
```

## Discussion

When you start a new search by calling the [`startSearchingForNewAccessories()`](./startsearchingfornewaccessories%28%29.md) method, HomeKit clears the [`discoveredAccessories`](./discoveredaccessories.md) array. It then modifies the array as it discovers new accessories until you end the search by calling the [`stopSearchingForNewAccessories()`](./stopsearchingfornewaccessories%28%29.md) method.

## See Also

### Discovering accessories
- [func startSearchingForNewAccessories()](./startsearchingfornewaccessories%28%29.md)
  Starts searching for accessories not yet associated with a home.
- [func stopSearchingForNewAccessories()](./stopsearchingfornewaccessories%28%29.md)
  Stops searching for new accessories.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmaccessorybrowser/discoveredaccessories)*