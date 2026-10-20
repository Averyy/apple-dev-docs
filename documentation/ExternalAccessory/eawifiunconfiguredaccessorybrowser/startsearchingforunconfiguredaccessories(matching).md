# startSearchingForUnconfiguredAccessories(matching:)

**Framework**: External Accessory  
**Kind**: method  
**Role**: Instance Method

Starts the search for unconfigured accessories that match the specified predicate.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
func startSearchingForUnconfiguredAccessories(matching predicate: NSPredicate?)
```

```objc
- (void) startSearchingForUnconfiguredAccessoriesMatchingPredicate:(NSPredicate *) predicate;
```

#### Discussion

This method starts a Wi-Fi scan for unconfigured accessories. Note that searching is a power and resource intensive process and must only be used when actively searching for accessories. As soon as the desired accessories have been located, you should immediately stop a search.

## Parameters

- `predicate`: The desired filter for unconfigured accessory results conforming to the [`EAWiFiUnconfiguredAccessoryBrowserDelegate`](../eawifiunconfiguredaccessorybrowserdelegate.md) protocol.

## See Also

### Finding and Configuring Accessories
- [func configureAccessory(EAWiFiUnconfiguredAccessory, withConfigurationUIOn: UIViewController)](./configureaccessory%28_,withconfigurationuion%29.md)
  Begins the configuration process for the specified accessory.
- [func stopSearchingForUnconfiguredAccessories()](./stopsearchingforunconfiguredaccessories%28%29.md)
  Stops the search for unconfigured accessories.
- [var unconfiguredAccessories: Set<EAWiFiUnconfiguredAccessory>](./unconfiguredaccessories.md)
  The set of unconfigured accessories that have been discovered.


---

*[View on Apple Developer](https://developer.apple.com/documentation/externalaccessory/eawifiunconfiguredaccessorybrowser/startsearchingforunconfiguredaccessories(matching:))*