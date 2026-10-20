# performEditingTransaction(for:using:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

**Availability**:
- macOS 12.0+

## Declaration

```swift
func performEditingTransaction(for textStorage: NSTextStorage, using transaction: () -> Void)
```

```objc
- (void) performEditingTransactionForTextStorage:(NSTextStorage *) textStorage usingBlock:(void (^)()) transaction;
```

## See Also

### Managing the editing process
- [func processEditing(for: NSTextStorage, edited: NSTextStorageEditActions, range: NSRange, changeInLength: Int, invalidatedRange: NSRange)](./processediting%28for,edited,range,changeinlength,invalidatedrange%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextstorageobserving/performeditingtransaction(for:using:))*