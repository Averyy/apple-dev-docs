# unconfiguredAccessories

**Framework**: External Accessory  
**Kind**: property

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

#### Discussion

The set of accessories in this property represents a snapshot that includes only those objects that match the filter predicate defined when starting the search. You can think of this property as representing the primary list of unconfigured accessories that have been found. Note that the [`accessoryBrowser(_:didFindUnconfiguredAccessories:)`](eawifiunconfiguredaccessorybrowserdelegate/accessorybrowser(_:didfindunconfiguredaccessories:).md) delegate method is called when accessories are added to this list; similarly, [`accessoryBrowser(_:didRemoveUnconfiguredAccessories:)`](eawifiunconfiguredaccessorybrowserdelegate/accessorybrowser(_:didremoveunconfiguredaccessories:).md) is called when accessories are removed from this list.

## See Also

- [func configureAccessory(EAWiFiUnconfiguredAccessory, withConfigurationUIOn: UIViewController)](eawifiunconfiguredaccessorybrowser/configureaccessory(_:withconfigurationuion:).md)
  Begins the configuration process for the specified accessory.
- [func startSearchingForUnconfiguredAccessories(matching: NSPredicate?)](eawifiunconfiguredaccessorybrowser/startsearchingforunconfiguredaccessories(matching:).md)
  Starts the search for unconfigured accessories that match the specified predicate.
- [func stopSearchingForUnconfiguredAccessories()](eawifiunconfiguredaccessorybrowser/stopsearchingforunconfiguredaccessories.md)
  Stops the search for unconfigured accessories.


---

*[View on Apple Developer](https://developer.apple.com/documentation/externalaccessory/eawifiunconfiguredaccessorybrowser/unconfiguredaccessories)*