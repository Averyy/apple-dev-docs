# unconfiguredAccessories

**Framework**: External Accessory  
**Kind**: property  
**Role**: Instance Property

The set of unconfigured accessories that have been discovered.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
var unconfiguredAccessories: Set<EAWiFiUnconfiguredAccessory> { get }
```

```objc
@property (atomic, copy, readonly) NSSet<EAWiFiUnconfiguredAccessory *> * unconfiguredAccessories;
```

## Discussion

The set of accessories in this property represents a snapshot that includes only those objects that match the filter predicate defined when starting the search. You can think of this property as representing the primary list of unconfigured accessories that have been found. Note that the [`accessoryBrowser(_:didFindUnconfiguredAccessories:)`](../eawifiunconfiguredaccessorybrowserdelegate/accessorybrowser%28_,didfindunconfiguredaccessories%29.md) delegate method is called when accessories are added to this list; similarly, [`accessoryBrowser(_:didRemoveUnconfiguredAccessories:)`](../eawifiunconfiguredaccessorybrowserdelegate/accessorybrowser%28_,didremoveunconfiguredaccessories%29.md) is called when accessories are removed from this list.

## See Also

### Finding and Configuring Accessories
- [func configureAccessory(EAWiFiUnconfiguredAccessory, withConfigurationUIOn: UIViewController)](./configureaccessory%28_,withconfigurationuion%29.md)
  Begins the configuration process for the specified accessory.
- [func startSearchingForUnconfiguredAccessories(matching: NSPredicate?)](./startsearchingforunconfiguredaccessories%28matching%29.md)
  Starts the search for unconfigured accessories that match the specified predicate.
- [func stopSearchingForUnconfiguredAccessories()](./stopsearchingforunconfiguredaccessories%28%29.md)
  Stops the search for unconfigured accessories.


---

*[View on Apple Developer](https://developer.apple.com/documentation/externalaccessory/eawifiunconfiguredaccessorybrowser/unconfiguredaccessories)*