# sizingOptions

**Framework**: SwiftUI  
**Kind**: property  
**Role**: Instance Property

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

## Discussion

The default value is the empty set.

## See Also

### Managing the size
- [func preferredContentSizeDidChange(forChildContentContainer: any UIContentContainer)](./preferredcontentsizedidchange%28forchildcontentcontainer%29.md)
- [func sizeThatFits(in: CGSize) -> CGSize](./sizethatfits%28in%29.md)
  Calculates and returns the most appropriate size for the current view.
- [var safeAreaRegions: SafeAreaRegions](./safearearegions.md)
  The safe area regions that this view controller adds to its view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/uihostingcontroller/sizingoptions)*