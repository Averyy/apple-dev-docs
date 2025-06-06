# delegate

**Framework**: UIKit  
**Kind**: property

The delegate for the text storage object.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
weak var delegate: (any NSTextStorageDelegate)? { get set }
```

#### Discussion

Use a delegate object to monitor edits occurring to the text contents. Your delegate object must conform to the [`NSTextStorageDelegate`](nstextstoragedelegate.md) protocol.

## See Also

- [protocol NSTextStorageDelegate](nstextstoragedelegate.md)
  The optional methods that delegates of text storage objects implement to handle text-edit processing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nstextstorage/delegate)*