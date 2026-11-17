# mapTemplate(_:didReceiveRequestForDestination:)

**Framework**: CarPlay  
**Kind**: method  
**Role**: Instance Method

Called when a navigation request is received. Show a trip preview corresponding to this destination and start navigation if the destination is accepted by the user.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+
- Mac Catalyst 26.4+

## Declaration

```swift
optional func mapTemplate(_ mapTemplate: CPMapTemplate, didReceiveRequestForDestination waypoint: CPNavigationWaypoint)
```

```objc
- (void) mapTemplate:(CPMapTemplate *) mapTemplate didReceiveRequestForDestination:(CPNavigationWaypoint *) waypoint;
```

## See Also

### Updating routes, stops, and destinations
- [func mapTemplate(CPMapTemplate, didRequestToRemoveDestination: CPNavigationWaypoint)](./maptemplate%28_,didrequesttoremovedestination%29.md)
  Called when the user removes the waypoint corresponding to the trip’s destination. Perform a reroute to update both the trip and route accordingly.
- [func mapTemplate(CPMapTemplate, didReceiveUpdatedRouteSource: CPRouteSource)](./maptemplate%28_,didreceiveupdatedroutesource%29.md)
  Called when the route source status has been updated by the built-in system.
- [func mapTemplateShouldProvideMultiStopRouting(CPMapTemplate) -> Bool](./maptemplateshouldprovidemultistoprouting%28_%29.md)
  Determines if the template should provide UI for multi-stop routing while actively navigating, including the ability to add and remove stops.
- [func mapTemplate(CPMapTemplate, didRequestMultiStopCardConfigurationWithCompletion: (CPMultiStopCardConfiguration) -> Void)](./maptemplate%28_,didrequestmultistopcardconfigurationwithcompletion%29.md)
  Called when the user requests multi-stop card to be displayed via tapping ETA tray.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpmaptemplatedelegate/maptemplate(_:didreceiverequestfordestination:))*