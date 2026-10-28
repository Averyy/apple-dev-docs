# delegate

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The delegate for the text storage object.

**Availability**:
- macOS 10.0+

## Declaration

```swift
weak var delegate: (any NSTextStorageDelegate)? { get set }
```

```objc
@property (weak, nullable) id<NSTextStorageDelegate> delegate;
```

## Discussion

Use a delegate object to monitor edits occurring to the text contents. Your delegate object must conform to the [`NSTextStorageDelegate`](../nstextstoragedelegate.md) protocol.

## See Also

### Processing the editing actions
- [protocol NSTextStorageDelegate](../nstextstoragedelegate.md)
  The optional methods that delegates of text storage objects implement to handle text-edit processing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextstorage/delegate)*