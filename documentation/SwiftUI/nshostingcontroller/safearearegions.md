# safeAreaRegions

**Framework**: SwiftUI  
**Kind**: property

The safe area regions that this view controller adds to its view.

**Availability**:
- macOS 13.3+

## Declaration

```swift
@MainActor
@preconcurrency var safeAreaRegions: SafeAreaRegions { get set }
```

#### Discussion

The default value is `SafeAreaRegions.all`.

## See Also

- [func sizeThatFits(in: CGSize) -> CGSize](nshostingcontroller/sizethatfits(in:).md)
  Calculates and returns the most appropriate size for the current view.
- [var preferredContentSize: NSSize](nshostingcontroller/preferredcontentsize.md)
- [var sizingOptions: NSHostingSizingOptions](nshostingcontroller/sizingoptions.md)
  The options for how the hosting controller’s view creates and updates constraints based on the size of its SwiftUI content.
- [var sceneBridgingOptions: NSHostingSceneBridgingOptions](nshostingcontroller/scenebridgingoptions.md)
  The options for which aspects of the window will be managed by this controller’s hosting view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/nshostingcontroller/safearearegions)*