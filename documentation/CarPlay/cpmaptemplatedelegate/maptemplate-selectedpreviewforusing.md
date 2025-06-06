# mapTemplate(_:selectedPreviewFor:using:)

**Framework**: CarPlay  
**Kind**: method

Tells the delegate that the user selected a trip and route choice to preview.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
optional func mapTemplate(_ mapTemplate: CPMapTemplate, selectedPreviewFor trip: CPTrip, using routeChoice: CPRouteChoice)
```

## Parameters

- `mapTemplate`: The current map template.
- `trip`: The selected trip.
- `routeChoice`: The route chosen by the user.

## See Also

- [func mapTemplate(CPMapTemplate, startedTrip: CPTrip, using: CPRouteChoice)](cpmaptemplatedelegate/maptemplate(_:startedtrip:using:).md)
  Tells the delegate that the user selected a trip and route choice to navigate.
- [func mapTemplateDidCancelNavigation(CPMapTemplate)](cpmaptemplatedelegate/maptemplatedidcancelnavigation(_:).md)
  Tells the delegate that the system canceled the navigation.
- [func mapTemplateShouldProvideNavigationMetadata(CPMapTemplate) -> Bool](cpmaptemplatedelegate/maptemplateshouldprovidenavigationmetadata(_:).md)
  Asks the delegate whether the template should provide navigation metadata


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpmaptemplatedelegate/maptemplate(_:selectedpreviewfor:using:))*