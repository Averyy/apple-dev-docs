# mapTemplateShouldProvideMultiStopRouting(_:)

**Framework**: CarPlay  
**Kind**: method  
**Role**: Instance Method

Determines if the template should provide UI for multi-stop routing while actively navigating, including the ability to add and remove stops.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+

## Declaration

```swift
optional func mapTemplateShouldProvideMultiStopRouting(_ mapTemplate: CPMapTemplate) -> Bool
```

```objc
- (BOOL) mapTemplateShouldProvideMultiStopRouting:(CPMapTemplate *) mapTemplate;
```

## Return Value

YES if the template should provide multi-stop routing functionalities, otherwise NO

## See Also

### Updating routes, stops, and destinations
- [func mapTemplate(CPMapTemplate, didReceiveRequestForDestination: CPNavigationWaypoint)](./maptemplate%28_,didreceiverequestfordestination%29.md)
  Called when a navigation request is received. Show a trip preview corresponding to this destination and start navigation if the destination is accepted by the user.
- [func mapTemplate(CPMapTemplate, didRequestToRemoveDestination: CPNavigationWaypoint)](./maptemplate%28_,didrequesttoremovedestination%29.md)
  Called when the user removes the waypoint corresponding to the trip’s destination. Perform a reroute to update both the trip and route accordingly.
- [func mapTemplate(CPMapTemplate, didReceiveUpdatedRouteSource: CPRouteSource)](./maptemplate%28_,didreceiveupdatedroutesource%29.md)
  Called when the route source status has been updated by the built-in system.
- [func mapTemplate(CPMapTemplate, didRequestMultiStopCardConfigurationWithCompletion: (CPMultiStopCardConfiguration) -> Void)](./maptemplate%28_,didrequestmultistopcardconfigurationwithcompletion%29.md)
  Called when the user requests multi-stop card to be displayed via tapping ETA tray.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpmaptemplatedelegate/maptemplateshouldprovidemultistoprouting(_:))*