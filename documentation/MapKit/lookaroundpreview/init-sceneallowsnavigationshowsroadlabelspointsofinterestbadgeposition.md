# init(scene:allowsNavigation:showsRoadLabels:pointsOfInterest:badgePosition:)

**Framework**: MapKit  
**Kind**: init

Creates a Look Around preview with a binding to a scene, navigation, road label, points of interest, and badge position you specify.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst ?+
- macOS 14.0+
- visionOS ?+

## Declaration

```swift
@MainActor
@preconcurrency init(scene: Binding<MKLookAroundScene?>, allowsNavigation: Bool = true, showsRoadLabels: Bool = true, pointsOfInterest: PointOfInterestCategories = .all, badgePosition: MKLookAroundBadgePosition = .topLeading)
```

#### Discussion

Navigation refers to the ability to tap-to-navigate to a different vantage point in the Look Around scene and what a person can control through the use of the `allowsNavigation` property. The framework refers to the ability to pan and zoom around the Look Around scene is as  and you can’t restrict it while in the Look Around viewer.

The Look Around viewer isn’t available on macOS and `allowsNavigation` has no effect; in iOS, exploration is always available in the Look Around viewer and you can’t disable it.

## Parameters

- `scene`: A binding to the Look Around scene to display.
- `allowsNavigation`: A Boolean value that indicates whether the Look Around scene allows navigation after the user taps the Look Around preview to enter the full screen Look Around viewer. MapKit never allows navigation on the Look Around preview itself.
- `showsRoadLabels`: A Boolean value that indicates whether the Look Around scene shows road labels after the user taps the Look Around preview to enter the full screen Look Around viewer. MapKit never shows road labels on the Look Around preview itself.
- `pointsOfInterest`: The categories of points of interest to display after the user taps the Look Around preview to enter the full screen Look Around viewer. MapKit never displays points of interest on the Look Around preview itself. By default, MapKit displays all points of interest categories.
- `badgePosition`: A value that controls the position of a badge on the Look Around preview.

## See Also

- [init(initialScene: MKLookAroundScene?, allowsNavigation: Bool, showsRoadLabels: Bool, pointsOfInterest: PointOfInterestCategories, badgePosition: MKLookAroundBadgePosition)](lookaroundpreview/init(initialscene:allowsnavigation:showsroadlabels:pointsofinterest:badgeposition:).md)
  Creates a Look Around preview with an initial scene, navigation, road label, points of interest, and badge position you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/lookaroundpreview/init(scene:allowsnavigation:showsroadlabels:pointsofinterest:badgeposition:))*