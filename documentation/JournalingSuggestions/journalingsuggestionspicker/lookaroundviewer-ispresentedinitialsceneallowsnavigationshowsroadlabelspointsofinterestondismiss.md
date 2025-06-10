# lookAroundViewer(isPresented:initialScene:allowsNavigation:showsRoadLabels:pointsOfInterest:onDismiss:)

**Framework**: Journaling Suggestions  
**Kind**: method

**Availability**:
- iOS 17.0+

## Declaration

```swift
@MainActor
@preconcurrency func lookAroundViewer(isPresented: Binding<Bool>, initialScene: MKLookAroundScene?, allowsNavigation: Bool = true, showsRoadLabels: Bool = true, pointsOfInterest: PointOfInterestCategories = .all, onDismiss: (() -> Void)? = nil) -> some View
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/journalingsuggestions/journalingsuggestionspicker/lookaroundviewer(ispresented:initialscene:allowsnavigation:showsroadlabels:pointsofinterest:ondismiss:))*