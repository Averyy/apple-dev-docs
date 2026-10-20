# delegate

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The animation delegate.

**Availability**:
- macOS

## Declaration

```swift
weak var delegate: (any NSAnimationDelegate)? { get set }
```

```objc
@property (weak, nullable) id<NSAnimationDelegate> delegate;
```

#### Discussion

The delegate must conform to the [`NSAnimationDelegate`](../nsanimationdelegate.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsanimation/delegate)*