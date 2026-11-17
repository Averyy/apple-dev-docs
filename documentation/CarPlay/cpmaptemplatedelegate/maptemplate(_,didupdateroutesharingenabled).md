# mapTemplate(_:didUpdateRouteSharingEnabled:)

**Framework**: CarPlay  
**Kind**: method  
**Role**: Instance Method

Called when the route sharing enabled status has been updated by the built-in system. Route sharing enabled is set to true when any vehicle features are enabled that rely on a route provided by the built‑in navigation system to func‑ tion.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+

## Declaration

```swift
optional func mapTemplate(_ mapTemplate: CPMapTemplate, didUpdateRouteSharingEnabled enabled: Bool)
```

```objc
- (void) mapTemplate:(CPMapTemplate *) mapTemplate didUpdateRouteSharingEnabled:(BOOL) enabled;
```

## See Also

### Sharing routes and destinations
- [func mapTemplateShouldProvideRouteSharing(CPMapTemplate) -> Bool](./maptemplateshouldprovideroutesharing%28_%29.md)
  Determines if the template should provide route sharing information to the vehicle. Apps that participate in route sharing will donate navigation information to the vehicle including the current route, a list of waypoints, and other metadata that allows the vehicle to track the user’s preferred route to their destination.
- [func mapTemplate(CPMapTemplate, willShareDestinationFor: CPTrip)](./maptemplate%28_,willsharedestinationfor%29.md)
  Called when a trip’s destination is about to be shared to the vehicle
- [func mapTemplate(CPMapTemplate, didShareDestinationFor: CPTrip)](./maptemplate%28_,didsharedestinationfor%29.md)
  Called when a vehicle successfully handled a shared trip’s destination
- [func mapTemplate(CPMapTemplate, didFailToShareDestinationFor: CPTrip, error: any Error)](./maptemplate%28_,didfailtosharedestinationfor,error%29.md)
  Called when a vehicle failed to handle a shared trip’s destination


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpmaptemplatedelegate/maptemplate(_:didupdateroutesharingenabled:))*