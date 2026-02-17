# mapTemplate(_:didReceiveRequestForDestination:)

**Framework**: CarPlay  
**Kind**: method

Called when a navigation request is received. Show a trip preview corresponding to this destination and start navigation if the destination is accepted by the user.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
optional func mapTemplate(_ mapTemplate: CPMapTemplate, didReceiveRequestForDestination waypoint: CPNavigationWaypoint)
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpmaptemplatedelegate/maptemplate(_:didreceiverequestfordestination:))*