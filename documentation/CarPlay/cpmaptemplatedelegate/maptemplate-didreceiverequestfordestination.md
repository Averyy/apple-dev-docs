# mapTemplate(_:didReceiveRequestForDestination:)

**Framework**: CarPlay  
**Kind**: method

Called when a navigation request is received. Show a trip preview corresponding to this destination and start navigation if the destination is accepted by the user.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+
- Mac Catalyst 26.4+

## Declaration

```swift
optional func mapTemplate(_ mapTemplate: CPMapTemplate, didReceiveRequestForDestination waypoint: CPNavigationWaypoint)
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpmaptemplatedelegate/maptemplate(_:didreceiverequestfordestination:))*