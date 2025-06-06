# preferredContentSize

**Framework**: SwiftUI  
**Kind**: property

**Availability**:
- macOS 10.15+

## Declaration

```swift
@MainActor
@preconcurrency override dynamic var preferredContentSize: NSSize { get set }
```

## See Also

- [func sizeThatFits(in: CGSize) -> CGSize](nshostingcontroller/sizethatfits(in:).md)
  Calculates and returns the most appropriate size for the current view.
- [var sizingOptions: NSHostingSizingOptions](nshostingcontroller/sizingoptions.md)
  The options for how the hosting controller’s view creates and updates constraints based on the size of its SwiftUI content.
- [var safeAreaRegions: SafeAreaRegions](nshostingcontroller/safearearegions.md)
  The safe area regions that this view controller adds to its view.
- [var sceneBridgingOptions: NSHostingSceneBridgingOptions](nshostingcontroller/scenebridgingoptions.md)
  The options for which aspects of the window will be managed by this controller’s hosting view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/nshostingcontroller/preferredcontentsize)*