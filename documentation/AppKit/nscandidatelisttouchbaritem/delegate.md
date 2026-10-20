# delegate

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The delegate of the candidate list item.

**Availability**:
- macOS 10.12.2+

## Declaration

```swift
weak var delegate: (any NSCandidateListTouchBarItemDelegate)? { get set }
```

```objc
@property (weak, nullable) id<NSCandidateListTouchBarItemDelegate> delegate;
```

## See Also

### Providing a client and a delegate
- [var client: (any NSView & NSTextInputClient)?](./client.md)
  The client object for the candidate list item.
- [protocol NSCandidateListTouchBarItemDelegate](../nscandidatelisttouchbaritemdelegate.md)
  A set of methods that a candidate list item delegate uses to enable selection state and list visibility.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscandidatelisttouchbaritem/delegate)*