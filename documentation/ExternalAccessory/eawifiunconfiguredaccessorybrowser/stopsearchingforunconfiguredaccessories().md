# stopSearchingForUnconfiguredAccessories()

**Framework**: External Accessory  
**Kind**: method  
**Role**: Instance Method

Stops the search for unconfigured accessories.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
func stopSearchingForUnconfiguredAccessories()
```

```objc
- (void) stopSearchingForUnconfiguredAccessories;
```

## See Also

### Finding and Configuring Accessories
- [func configureAccessory(EAWiFiUnconfiguredAccessory, withConfigurationUIOn: UIViewController)](./configureaccessory%28_,withconfigurationuion%29.md)
  Begins the configuration process for the specified accessory.
- [func startSearchingForUnconfiguredAccessories(matching: NSPredicate?)](./startsearchingforunconfiguredaccessories%28matching%29.md)
  Starts the search for unconfigured accessories that match the specified predicate.
- [var unconfiguredAccessories: Set<EAWiFiUnconfiguredAccessory>](./unconfiguredaccessories.md)
  The set of unconfigured accessories that have been discovered.


---

*[View on Apple Developer](https://developer.apple.com/documentation/externalaccessory/eawifiunconfiguredaccessorybrowser/stopsearchingforunconfiguredaccessories())*