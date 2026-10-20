# mapTemplate(_:startedTrip:using:)

**Framework**: CarPlay  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that the user selected a trip and route choice to navigate.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
optional func mapTemplate(_ mapTemplate: CPMapTemplate, startedTrip trip: CPTrip, using routeChoice: CPRouteChoice)
```

```objc
- (void) mapTemplate:(CPMapTemplate *) mapTemplate startedTrip:(CPTrip *) trip usingRouteChoice:(CPRouteChoice *) routeChoice;
```

## Parameters

- `mapTemplate`: The current map template.
- `trip`: The selected trip.
- `routeChoice`: The selected route choice.

## See Also

### Handling Navigation Events
- [func mapTemplate(CPMapTemplate, selectedPreviewFor: CPTrip, using: CPRouteChoice)](./maptemplate%28_,selectedpreviewfor,using%29.md)
  Tells the delegate that the user selected a trip and route choice to preview.
- [func mapTemplateDidCancelNavigation(CPMapTemplate)](./maptemplatedidcancelnavigation%28_%29.md)
  Tells the delegate that the system canceled the navigation.
- [func mapTemplateShouldProvideNavigationMetadata(CPMapTemplate) -> Bool](./maptemplateshouldprovidenavigationmetadata%28_%29.md)
  Asks the delegate whether the template should provide navigation metadata


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpmaptemplatedelegate/maptemplate(_:startedtrip:using:))*