# accessoryBrowser(_:didFindUnconfiguredAccessories:)

**Framework**: External Accessory  
**Kind**: method  
**Required**: Yes

Indicates that the browser found a new unconfigured accessory that matches the filter predicate defined at the start of the search.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
func accessoryBrowser(_ browser: EAWiFiUnconfiguredAccessoryBrowser, didFindUnconfiguredAccessories accessories: Set<EAWiFiUnconfiguredAccessory>)
```

#### Discussion

When a new unconfigured accessory is found, it’s added to the browser’s set of accessories, which is available in the [`unconfiguredAccessories`](eawifiunconfiguredaccessorybrowser/unconfiguredaccessories.md) property. A delegate can implement this method to present to the user the current list of unconfigured accessories. Because this method is called every time a new unconfigured accessory is found, you might use this callback as a prompt to check the list of accessories in [`unconfiguredAccessories`](eawifiunconfiguredaccessorybrowser/unconfiguredaccessories.md).

## Parameters

- `browser`: The instance of   that is generating the event.
- `accessories`: The set of   objects that have been found since the last update.

## See Also

- [func accessoryBrowser(EAWiFiUnconfiguredAccessoryBrowser, didRemoveUnconfiguredAccessories: Set<EAWiFiUnconfiguredAccessory>)](eawifiunconfiguredaccessorybrowserdelegate/accessorybrowser(_:didremoveunconfiguredaccessories:).md)
  Indicates that the browser removed an unconfigured accessory from the search results.


---

*[View on Apple Developer](https://developer.apple.com/documentation/externalaccessory/eawifiunconfiguredaccessorybrowserdelegate/accessorybrowser(_:didfindunconfiguredaccessories:))*