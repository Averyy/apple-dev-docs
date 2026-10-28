# scrollContent

**Framework**: SwiftUI  
**Kind**: property  
**Role**: Type Property

The scroll content placement.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
static var scrollContent: ContentMarginPlacement { get }
```

## Discussion

Scrollable views like [`ScrollView`](../scrollview.md) will use this placement to inset their content, but not their scroll indicators.

## See Also

### Getting the placement
- [static var automatic: ContentMarginPlacement](./automatic.md)
  The automatic placement.
- [static var scrollIndicators: ContentMarginPlacement](./scrollindicators.md)
  The scroll indicators placement.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/contentmarginplacement/scrollcontent)*