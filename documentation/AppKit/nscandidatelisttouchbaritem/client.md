# client

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The client object for the candidate list item.

**Availability**:
- macOS 10.12.2+

## Declaration

```swift
weak var client: (any NSView & NSTextInputClient)? { get set }
```

```objc
@property (weak, nullable) NSView<NSTextInputClient> * client;
```

## Discussion

This object must be a subclass of [`NSView`](../nsview.md) and adopt the [`NSTextInputClient`](../nstextinputclient.md) protocol.

The candidate list item uses this property to show completion candidates as users enter text. You can disable this behavior with the [`allowsTextInputContextCandidates`](./allowstextinputcontextcandidates.md) property.

## See Also

### Providing a client and a delegate
- [var delegate: (any NSCandidateListTouchBarItemDelegate)?](./delegate.md)
  The delegate of the candidate list item.
- [protocol NSCandidateListTouchBarItemDelegate](../nscandidatelisttouchbaritemdelegate.md)
  A set of methods that a candidate list item delegate uses to enable selection state and list visibility.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscandidatelisttouchbaritem/client)*