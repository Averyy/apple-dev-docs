# sizeThatFits(in:)

**Framework**: SwiftUI  
**Kind**: method

Calculates and returns the most appropriate size for the current view.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
@preconcurrency func sizeThatFits(in size: CGSize) -> CGSize
```

#### Return Value

The size that offers the best fit for the root view and its contents.

## Parameters

- `size`: The proposed new size for the view.

## See Also

- [var sizingOptions: UIHostingControllerSizingOptions](uihostingcontroller/sizingoptions.md)
  The options for how the hosting controller tracks changes to the size of its SwiftUI content.
- [func preferredContentSizeDidChange(forChildContentContainer: any UIContentContainer)](uihostingcontroller/preferredcontentsizedidchange(forchildcontentcontainer:).md)
- [var safeAreaRegions: SafeAreaRegions](uihostingcontroller/safearearegions.md)
  The safe area regions that this view controller adds to its view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/uihostingcontroller/sizethatfits(in:))*