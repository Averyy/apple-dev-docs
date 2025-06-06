# paging

**Framework**: SwiftUI  
**Kind**: property

The scroll behavior that aligns scroll targets to container-based geometry.

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
static var paging: PagingScrollTargetBehavior { get }
```

#### Discussion

In the following example, every view in the lazy stack is flexible in both directions and the scroll view settles to container-aligned boundaries.

```swift
ScrollView {
    LazyVStack(spacing: 0.0) {
        ForEach(items) { item in
            FullScreenItem(item)
        }
    }
}
.scrollTargetBehavior(.paging)
```

## See Also

- [static var viewAligned: ViewAlignedScrollTargetBehavior](scrolltargetbehavior/viewaligned.md)
  The scroll behavior that aligns scroll targets to view-based geometry.
- [static func viewAligned(limitBehavior: ViewAlignedScrollTargetBehavior.LimitBehavior) -> Self](scrolltargetbehavior/viewaligned(limitbehavior:).md)
  The scroll behavior that aligns scroll targets to view-based geometry.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/scrolltargetbehavior/paging)*