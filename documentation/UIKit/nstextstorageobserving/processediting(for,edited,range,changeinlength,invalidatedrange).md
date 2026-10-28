# processEditing(for:edited:range:changeInLength:invalidatedRange:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Notifies the observer that the text storage has been edited.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
func processEditing(for textStorage: NSTextStorage, edited editMask: NSTextStorage.EditActions, range newCharRange: NSRange, changeInLength delta: Int, invalidatedRange invalidatedCharRange: NSRange)
```

```objc
- (void) processEditingForTextStorage:(NSTextStorage *) textStorage edited:(NSTextStorageEditActions) editMask range:(NSRange) newCharRange changeInLength:(NSInteger) delta invalidatedRange:(NSRange) invalidatedCharRange;
```

## Discussion

The `newCharRange` is the range in the final string which was explicitly edited. The `invalidatedRange` includes portions that changed as a result of attribute fixing — it is either equal to `newCharRange` or larger. Controllers should not change the contents of the text storage during the execution of this message.

## Parameters

- `textStorage`: The text storage that was edited.
- `editMask`: The type of edit.
- `newCharRange`: The range of characters that changed.
- `delta`: The change in length.
- `invalidatedCharRange`: The full invalidated range including attribute fixing.

## See Also

### Managing the editing process
- [func performEditingTransaction(for: NSTextStorage, using: () -> Void)](./performeditingtransaction%28for,using%29.md)
  Performs an editing transaction on the text storage.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nstextstorageobserving/processediting(for:edited:range:changeinlength:invalidatedrange:))*