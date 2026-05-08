# automatic

**Framework**: SwiftUI  
**Kind**: property

The automatic placement.

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
static var automatic: ContentMarginPlacement { get }
```

#### Discussion

Views that support margin customization can automatically use margins with this placement. For example, a [`ScrollView`](scrollview.md) will use this placement to automatically inset both its content and scroll indicators by the specified amount.

## See Also

- [static var scrollContent: ContentMarginPlacement](contentmarginplacement/scrollcontent.md)
  The scroll content placement.
- [static var scrollIndicators: ContentMarginPlacement](contentmarginplacement/scrollindicators.md)
  The scroll indicators placement.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/contentmarginplacement/automatic)*