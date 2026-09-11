# mapTemplate(_:didRequestToRemoveDestination:)

**Framework**: CarPlay  
**Kind**: method

Called when the user removes the waypoint corresponding to the trip’s destination. Perform a reroute to update both the trip and route accordingly.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+

## Declaration

```swift
optional func mapTemplate(_ mapTemplate: CPMapTemplate, didRequestToRemoveDestination waypoint: CPNavigationWaypoint)
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpmaptemplatedelegate/maptemplate(_:didrequesttoremovedestination:))*