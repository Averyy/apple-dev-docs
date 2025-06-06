# sizingOptions

**Framework**: SwiftUI  
**Kind**: property

The options for how the hosting controller tracks changes to the size of its SwiftUI content.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
@preconcurrency var sizingOptions: UIHostingControllerSizingOptions { get set }
```

#### Discussion

The default value is the empty set.

## See Also

- [func preferredContentSizeDidChange(forChildContentContainer: any UIContentContainer)](uihostingcontroller/preferredcontentsizedidchange(forchildcontentcontainer:).md)
- [func sizeThatFits(in: CGSize) -> CGSize](uihostingcontroller/sizethatfits(in:).md)
  Calculates and returns the most appropriate size for the current view.
- [var safeAreaRegions: SafeAreaRegions](uihostingcontroller/safearearegions.md)
  The safe area regions that this view controller adds to its view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/uihostingcontroller/sizingoptions)*