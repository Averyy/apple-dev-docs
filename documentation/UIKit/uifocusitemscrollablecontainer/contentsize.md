# contentSize

**Framework**: UIKit  
**Kind**: property  
**Required**: Yes

The total size of the content contained by this container.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- tvOS 12.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var contentSize: CGSize { get }
```

#### Discussion

If the value of this property is larger than [`visibleSize`](uifocusitemscrollablecontainer/visiblesize.md) then the content is scrollable.

## See Also

- [var contentOffset: CGPoint](uifocusitemscrollablecontainer/contentoffset.md)
  The current content offset for the scrollable container.
- [var visibleSize: CGSize](uifocusitemscrollablecontainer/visiblesize.md)
  The visible size of the scrollable container.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uifocusitemscrollablecontainer/contentsize)*