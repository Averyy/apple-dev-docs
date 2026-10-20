# mapTemplate(_:didRequestToRemove:)

**Framework**: CarPlay  
**Kind**: method  
**Role**: Instance Method

Called when the user removes a waypoint. Perform a reroute to update the route accordingly.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+

## Declaration

```swift
optional func mapTemplate(_ mapTemplate: CPMapTemplate, didRequestToRemove waypoint: CPNavigationWaypoint)
```

```objc
- (void) mapTemplate:(CPMapTemplate *) mapTemplate didRequestToRemoveWaypoint:(CPNavigationWaypoint *) waypoint;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpmaptemplatedelegate/maptemplate(_:didrequesttoremove:))*