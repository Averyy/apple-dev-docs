# delegate

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The rule editor’s delegate.

**Availability**:
- macOS

## Declaration

```swift
weak var delegate: (any NSRuleEditorDelegate)? { get set }
```

```objc
@property (weak, nullable) id<NSRuleEditorDelegate> delegate;
```

## See Also

### Configuring the Delegate
- [protocol NSRuleEditorDelegate](../nsruleeditordelegate.md)
  The `NSRuleEditorDelegate` protocol defines the optional methods implemented by delegates of [`NSRuleEditor`](../nsruleeditor.md) objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsruleeditor/delegate)*