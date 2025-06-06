# accessoryBrowser(_:didRemoveUnconfiguredAccessories:)

**Framework**: External Accessory  
**Kind**: method  
**Required**: Yes

Indicates that the browser removed an unconfigured accessory from the search results.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
func accessoryBrowser(_ browser: EAWiFiUnconfiguredAccessoryBrowser, didRemoveUnconfiguredAccessories accessories: Set<EAWiFiUnconfiguredAccessory>)
```

#### Discussion

This method is called when the browser removes an accessory from the primary list of unconfigured accessories represented in its [`unconfiguredAccessories`](eawifiunconfiguredaccessorybrowser/unconfiguredaccessories.md) property. A delegate can implement this method to present to the user the current list of unconfigured accessories. Because this method is called every time an unconfigured accessory is removed from the list, you might use this callback as a prompt to check the list of accessories in [`unconfiguredAccessories`](eawifiunconfiguredaccessorybrowser/unconfiguredaccessories.md).

## Parameters

- `browser`: The instance of   that is generating the event.
- `accessories`: The set of   objects that have been removed from the scan results since the last update. The browser removes only accessories that match the filter predicate you specified at the start of the search.

## See Also

- [func accessoryBrowser(EAWiFiUnconfiguredAccessoryBrowser, didFindUnconfiguredAccessories: Set<EAWiFiUnconfiguredAccessory>)](eawifiunconfiguredaccessorybrowserdelegate/accessorybrowser(_:didfindunconfiguredaccessories:).md)
  Indicates that the browser found a new unconfigured accessory that matches the filter predicate defined at the start of the search.


---

*[View on Apple Developer](https://developer.apple.com/documentation/externalaccessory/eawifiunconfiguredaccessorybrowserdelegate/accessorybrowser(_:didremoveunconfiguredaccessories:))*