# mapTemplateShouldProvideRouteSharing(_:)

**Framework**: CarPlay  
**Kind**: method

Determines if the template should provide route sharing information to the vehicle. Apps that participate in route sharing will donate navigation information to the vehicle including the current route, a list of waypoints, and other metadata that allows the vehicle to track the user’s preferred route to their destination.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+
- Mac Catalyst 26.4+

## Declaration

```swift
optional func mapTemplateShouldProvideRouteSharing(_ mapTemplate: CPMapTemplate) -> Bool
```

#### Return Value

YES if the template should provide route sharing, otherwise NO


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpmaptemplatedelegate/maptemplateshouldprovideroutesharing(_:))*