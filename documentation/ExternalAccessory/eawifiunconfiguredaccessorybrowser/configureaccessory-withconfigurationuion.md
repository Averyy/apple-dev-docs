# configureAccessory(_:withConfigurationUIOn:)

**Framework**: External Accessory  
**Kind**: method

Begins the configuration process for the specified accessory.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
func configureAccessory(_ accessory: EAWiFiUnconfiguredAccessory, withConfigurationUIOn viewController: UIViewController)
```

#### Discussion

This method stops the search for unconfigured accessories and begins the configuration process of the specified accessory. To guide the user through the configuration process (which can take up to a few minutes to complete), the system displays a modal setup UI on top of the specified view controller. Upon completion of the process, the host app’s delegate receives the accessoryBrowser:didFinishConfiguringAccessory:withError: callback with a status value that it can check. For example, an app might want to tell the user if the configuration failed.

## Parameters

- `accessory`: The accessory the app is configuring.
- `viewController`: The view controller that will host the system-provided setup UI in the app. Typically,   is the same view controller the app is using to present its user interface at the time it calls this method.

## See Also

- [func startSearchingForUnconfiguredAccessories(matching: NSPredicate?)](eawifiunconfiguredaccessorybrowser/startsearchingforunconfiguredaccessories(matching:).md)
  Starts the search for unconfigured accessories that match the specified predicate.
- [func stopSearchingForUnconfiguredAccessories()](eawifiunconfiguredaccessorybrowser/stopsearchingforunconfiguredaccessories.md)
  Stops the search for unconfigured accessories.
- [var unconfiguredAccessories: Set<EAWiFiUnconfiguredAccessory>](eawifiunconfiguredaccessorybrowser/unconfiguredaccessories.md)
  The set of unconfigured accessories that have been discovered.


---

*[View on Apple Developer](https://developer.apple.com/documentation/externalaccessory/eawifiunconfiguredaccessorybrowser/configureaccessory(_:withconfigurationuion:))*