# mapTemplateShouldProvideRouteSharing(_:)

**Framework**: CarPlay  
**Kind**: method  
**Role**: Instance Method

Determines if the template should provide route sharing information to the vehicle. Apps that participate in route sharing will donate navigation information to the vehicle including the current route, a list of waypoints, and other metadata that allows the vehicle to track the user’s preferred route to their destination.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+
- Mac Catalyst 26.4+

## Declaration

```swift
optional func mapTemplateShouldProvideRouteSharing(_ mapTemplate: CPMapTemplate) -> Bool
```

```objc
- (BOOL) mapTemplateShouldProvideRouteSharing:(CPMapTemplate *) mapTemplate;
```

## Return Value

YES if the template should provide route sharing, otherwise NO

## See Also

### Sharing routes and destinations
- [func mapTemplate(CPMapTemplate, didUpdateRouteSharingEnabled: Bool)](./maptemplate%28_,didupdateroutesharingenabled%29.md)
  Called when the route sharing enabled status has been updated by the built-in system. Route sharing enabled is set to true when any vehicle features are enabled that rely on a route provided by the built‑in navigation system to func‑ tion.
- [func mapTemplate(CPMapTemplate, willShareDestinationFor: CPTrip)](./maptemplate%28_,willsharedestinationfor%29.md)
  Called when a trip’s destination is about to be shared to the vehicle
- [func mapTemplate(CPMapTemplate, didShareDestinationFor: CPTrip)](./maptemplate%28_,didsharedestinationfor%29.md)
  Called when a vehicle successfully handled a shared trip’s destination
- [func mapTemplate(CPMapTemplate, didFailToShareDestinationFor: CPTrip, error: any Error)](./maptemplate%28_,didfailtosharedestinationfor,error%29.md)
  Called when a vehicle failed to handle a shared trip’s destination


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpmaptemplatedelegate/maptemplateshouldprovideroutesharing(_:))*