# lookAroundViewer(isPresented:scene:allowsNavigation:showsRoadLabels:pointsOfInterest:onDismiss:)

**Framework**: Journaling Suggestions  
**Kind**: method

**Availability**:
- iOS 17.0+

## Declaration

```swift
@MainActor
@preconcurrency func lookAroundViewer(isPresented: Binding<Bool>, scene: Binding<MKLookAroundScene?>, allowsNavigation: Bool = true, showsRoadLabels: Bool = true, pointsOfInterest: PointOfInterestCategories = .all, onDismiss: (() -> Void)? = nil) -> some View
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/journalingsuggestions/journalingsuggestionspicker/lookaroundviewer(ispresented:scene:allowsnavigation:showsroadlabels:pointsofinterest:ondismiss:))*