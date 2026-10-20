# delegate

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The delegate for messages from the field editor.

**Availability**:
- macOS

## Declaration

```swift
weak var delegate: (any NSMatrixDelegate)? { get set }
```

```objc
@property (weak, nullable) id<NSMatrixDelegate> delegate;
```

## See Also

### Related Documentation
- [func textShouldEndEditing(NSText) -> Bool](./textshouldendediting%28_%29.md)
  Requests permission to end editing.
- [func textShouldBeginEditing(NSText) -> Bool](./textshouldbeginediting%28_%29.md)
  Requests permission to begin editing text.
### Managing the Delegate
- [protocol NSMatrixDelegate](../nsmatrixdelegate.md)
  The `NSMatrixDelegate` protocol defines the optional methods implemented by delegates of `NSMatrix` objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmatrix/delegate)*