# mapTemplateDidCancelNavigation(_:)

**Framework**: CarPlay  
**Kind**: method

Tells the delegate that the system canceled the navigation.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
optional func mapTemplateDidCancelNavigation(_ mapTemplate: CPMapTemplate)
```

## Parameters

- `mapTemplate`: The current map template.

## See Also

- [func mapTemplate(CPMapTemplate, selectedPreviewFor: CPTrip, using: CPRouteChoice)](cpmaptemplatedelegate/maptemplate(_:selectedpreviewfor:using:).md)
  Tells the delegate that the user selected a trip and route choice to preview.
- [func mapTemplate(CPMapTemplate, startedTrip: CPTrip, using: CPRouteChoice)](cpmaptemplatedelegate/maptemplate(_:startedtrip:using:).md)
  Tells the delegate that the user selected a trip and route choice to navigate.
- [func mapTemplateShouldProvideNavigationMetadata(CPMapTemplate) -> Bool](cpmaptemplatedelegate/maptemplateshouldprovidenavigationmetadata(_:).md)
  Asks the delegate whether the template should provide navigation metadata


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpmaptemplatedelegate/maptemplatedidcancelnavigation(_:))*