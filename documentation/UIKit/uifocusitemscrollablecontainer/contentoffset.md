# contentOffset

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

The current content offset for the scrollable container.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- tvOS 12.0+
- visionOS 1.0+

## Declaration

```swift
var contentOffset: CGPoint { get set }
```

```objc
@property (nonatomic, readwrite) CGPoint contentOffset;
```

## Discussion

If the scrollable container contains `bounds`, then `bounds.origin` must be equal to the content offset. The system repeatedly sets this property to simulate animated scrolling.

## See Also

### Retrieving the content size
- [var contentSize: CGSize](./contentsize.md)
  The total size of the content contained by this container.
- [var visibleSize: CGSize](./visiblesize.md)
  The visible size of the scrollable container.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uifocusitemscrollablecontainer/contentoffset)*