# processEditing(for:edited:range:changeInLength:invalidatedRange:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

**Availability**:
- macOS 12.0+

## Declaration

```swift
func processEditing(for textStorage: NSTextStorage, edited editMask: NSTextStorageEditActions, range newCharRange: NSRange, changeInLength delta: Int, invalidatedRange invalidatedCharRange: NSRange)
```

```objc
- (void) processEditingForTextStorage:(NSTextStorage *) textStorage edited:(NSTextStorageEditActions) editMask range:(NSRange) newCharRange changeInLength:(NSInteger) delta invalidatedRange:(NSRange) invalidatedCharRange;
```

## See Also

### Managing the editing process
- [func performEditingTransaction(for: NSTextStorage, using: () -> Void)](./performeditingtransaction%28for,using%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextstorageobserving/processediting(for:edited:range:changeinlength:invalidatedrange:))*