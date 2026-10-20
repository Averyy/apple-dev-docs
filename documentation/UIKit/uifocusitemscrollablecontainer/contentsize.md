# contentSize

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property  
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
var contentSize: CGSize { get }
```

```objc
@property (nonatomic, readonly) CGSize contentSize;
```

#### Discussion

If the value of this property is larger than [`visibleSize`](./visiblesize.md) then the content is scrollable.

## See Also

### Retrieving the content size
- [var contentOffset: CGPoint](./contentoffset.md)
  The current content offset for the scrollable container.
- [var visibleSize: CGSize](./visiblesize.md)
  The visible size of the scrollable container.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uifocusitemscrollablecontainer/contentsize)*