# mapTemplateShouldProvideNavigationMetadata(_:)

**Framework**: CarPlay  
**Kind**: method

Asks the delegate whether the template should provide navigation metadata

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+

## Declaration

```swift
@MainActor
optional func mapTemplateShouldProvideNavigationMetadata(_ mapTemplate: CPMapTemplate) -> Bool
```

#### Discussion

- Returns `true` if the template needs to provide navigation metadata, otherwise `false`.

## Parameters

- `mapTemplate`: The current map template.

## See Also

- [func mapTemplate(CPMapTemplate, selectedPreviewFor: CPTrip, using: CPRouteChoice)](cpmaptemplatedelegate/maptemplate(_:selectedpreviewfor:using:).md)
  Tells the delegate that the user selected a trip and route choice to preview.
- [func mapTemplate(CPMapTemplate, startedTrip: CPTrip, using: CPRouteChoice)](cpmaptemplatedelegate/maptemplate(_:startedtrip:using:).md)
  Tells the delegate that the user selected a trip and route choice to navigate.
- [func mapTemplateDidCancelNavigation(CPMapTemplate)](cpmaptemplatedelegate/maptemplatedidcancelnavigation(_:).md)
  Tells the delegate that the system canceled the navigation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpmaptemplatedelegate/maptemplateshouldprovidenavigationmetadata(_:))*