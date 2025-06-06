# preferredContentSizeDidChange(forChildContentContainer:)

**Framework**: SwiftUI  
**Kind**: method

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
@preconcurrency override dynamic func preferredContentSizeDidChange(forChildContentContainer container: any UIContentContainer)
```

## See Also

- [var sizingOptions: UIHostingControllerSizingOptions](uihostingcontroller/sizingoptions.md)
  The options for how the hosting controller tracks changes to the size of its SwiftUI content.
- [func sizeThatFits(in: CGSize) -> CGSize](uihostingcontroller/sizethatfits(in:).md)
  Calculates and returns the most appropriate size for the current view.
- [var safeAreaRegions: SafeAreaRegions](uihostingcontroller/safearearegions.md)
  The safe area regions that this view controller adds to its view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/uihostingcontroller/preferredcontentsizedidchange(forchildcontentcontainer:))*