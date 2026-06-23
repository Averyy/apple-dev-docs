# performEditingTransaction(for:using:)

**Framework**: UIKit  
**Kind**: method  
**Required**: Yes

Performs an editing transaction on the text storage.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
func performEditingTransaction(for textStorage: NSTextStorage, using transaction: () -> Void)
```

## Parameters

- `textStorage`: The text storage.
- `transaction`: The block to execute within the transaction.

## See Also

- [func processEditing(for: NSTextStorage, edited: NSTextStorage.EditActions, range: NSRange, changeInLength: Int, invalidatedRange: NSRange)](nstextstorageobserving/processediting(for:edited:range:changeinlength:invalidatedrange:).md)
  Notifies the observer that the text storage has been edited.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nstextstorageobserving/performeditingtransaction(for:using:))*