# mapTemplateDidCancelNavigation(_:)

**Framework**: CarPlay  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that the system canceled the navigation.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
optional func mapTemplateDidCancelNavigation(_ mapTemplate: CPMapTemplate)
```

```objc
- (void) mapTemplateDidCancelNavigation:(CPMapTemplate *) mapTemplate;
```

## Parameters

- `mapTemplate`: The current map template.

## See Also

### Handling Navigation Events
- [func mapTemplate(CPMapTemplate, selectedPreviewFor: CPTrip, using: CPRouteChoice)](./maptemplate%28_,selectedpreviewfor,using%29.md)
  Tells the delegate that the user selected a trip and route choice to preview.
- [func mapTemplate(CPMapTemplate, startedTrip: CPTrip, using: CPRouteChoice)](./maptemplate%28_,startedtrip,using%29.md)
  Tells the delegate that the user selected a trip and route choice to navigate.
- [func mapTemplateShouldProvideNavigationMetadata(CPMapTemplate) -> Bool](./maptemplateshouldprovidenavigationmetadata%28_%29.md)
  Asks the delegate whether the template should provide navigation metadata


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpmaptemplatedelegate/maptemplatedidcancelnavigation(_:))*