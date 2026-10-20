# mapTemplateShouldProvideNavigationMetadata(_:)

**Framework**: CarPlay  
**Kind**: method  
**Role**: Instance Method

Asks the delegate whether the template should provide navigation metadata

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+

## Declaration

```swift
optional func mapTemplateShouldProvideNavigationMetadata(_ mapTemplate: CPMapTemplate) -> Bool
```

```objc
- (BOOL) mapTemplateShouldProvideNavigationMetadata:(CPMapTemplate *) mapTemplate;
```

#### Discussion

- Returns `true` if the template needs to provide navigation metadata, otherwise `false`.

## Parameters

- `mapTemplate`: The current map template.

## See Also

### Handling Navigation Events
- [func mapTemplate(CPMapTemplate, selectedPreviewFor: CPTrip, using: CPRouteChoice)](./maptemplate%28_,selectedpreviewfor,using%29.md)
  Tells the delegate that the user selected a trip and route choice to preview.
- [func mapTemplate(CPMapTemplate, startedTrip: CPTrip, using: CPRouteChoice)](./maptemplate%28_,startedtrip,using%29.md)
  Tells the delegate that the user selected a trip and route choice to navigate.
- [func mapTemplateDidCancelNavigation(CPMapTemplate)](./maptemplatedidcancelnavigation%28_%29.md)
  Tells the delegate that the system canceled the navigation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpmaptemplatedelegate/maptemplateshouldprovidenavigationmetadata(_:))*