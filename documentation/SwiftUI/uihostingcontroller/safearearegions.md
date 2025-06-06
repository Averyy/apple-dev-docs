# safeAreaRegions

**Framework**: SwiftUI  
**Kind**: property

The safe area regions that this view controller adds to its view.

**Availability**:
- iOS 16.4+
- iPadOS 16.4+
- Mac Catalyst 16.4+
- tvOS 16.4+
- visionOS 1.0+

## Declaration

```swift
@MainActor
@preconcurrency var safeAreaRegions: SafeAreaRegions { get set }
```

#### Discussion

An example of when this is appropriate to use is when hosting content that you know should never be affected by the safe area, such as a custom scrollable container. Disabling a safe area region omits it from the SwiftUI layout system altogether.

The default value is `SafeAreaRegions.all`.

## See Also

- [var sizingOptions: UIHostingControllerSizingOptions](uihostingcontroller/sizingoptions.md)
  The options for how the hosting controller tracks changes to the size of its SwiftUI content.
- [func preferredContentSizeDidChange(forChildContentContainer: any UIContentContainer)](uihostingcontroller/preferredcontentsizedidchange(forchildcontentcontainer:).md)
- [func sizeThatFits(in: CGSize) -> CGSize](uihostingcontroller/sizethatfits(in:).md)
  Calculates and returns the most appropriate size for the current view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/uihostingcontroller/safearearegions)*