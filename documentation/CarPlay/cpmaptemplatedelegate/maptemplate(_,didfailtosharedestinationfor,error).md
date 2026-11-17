# mapTemplate(_:didFailToShareDestinationFor:error:)

**Framework**: CarPlay  
**Kind**: method  
**Role**: Instance Method

Called when a vehicle failed to handle a shared trip’s destination

**Availability**:
- iOS 26.4+
- iPadOS 26.4+
- Mac Catalyst 26.4+

## Declaration

```swift
optional func mapTemplate(_ mapTemplate: CPMapTemplate, didFailToShareDestinationFor trip: CPTrip, error: any Error)
```

```objc
- (void) mapTemplate:(CPMapTemplate *) mapTemplate didFailToShareDestinationForTrip:(CPTrip *) trip error:(NSError *) error;
```

## See Also

### Sharing routes and destinations
- [func mapTemplateShouldProvideRouteSharing(CPMapTemplate) -> Bool](./maptemplateshouldprovideroutesharing%28_%29.md)
  Determines if the template should provide route sharing information to the vehicle. Apps that participate in route sharing will donate navigation information to the vehicle including the current route, a list of waypoints, and other metadata that allows the vehicle to track the user’s preferred route to their destination.
- [func mapTemplate(CPMapTemplate, didUpdateRouteSharingEnabled: Bool)](./maptemplate%28_,didupdateroutesharingenabled%29.md)
  Called when the route sharing enabled status has been updated by the built-in system. Route sharing enabled is set to true when any vehicle features are enabled that rely on a route provided by the built‑in navigation system to func‑ tion.
- [func mapTemplate(CPMapTemplate, willShareDestinationFor: CPTrip)](./maptemplate%28_,willsharedestinationfor%29.md)
  Called when a trip’s destination is about to be shared to the vehicle
- [func mapTemplate(CPMapTemplate, didShareDestinationFor: CPTrip)](./maptemplate%28_,didsharedestinationfor%29.md)
  Called when a vehicle successfully handled a shared trip’s destination


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpmaptemplatedelegate/maptemplate(_:didfailtosharedestinationfor:error:))*