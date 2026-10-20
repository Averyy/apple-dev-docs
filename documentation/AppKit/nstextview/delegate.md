# delegate

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The delegate for all text views sharing the receiver’s layout manager.

**Availability**:
- macOS

## Declaration

```swift
weak var delegate: (any NSTextViewDelegate)? { get set }
```

```objc
@property (weak, nullable) id<NSTextViewDelegate> delegate;
```

## See Also

### Managing the text view’s content
- [protocol NSTextViewDelegate](../nstextviewdelegate.md)
  A set of optional methods that text view delegates can use to manage selection, set text attributes, work with the spell checker, and more.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextview/delegate)*