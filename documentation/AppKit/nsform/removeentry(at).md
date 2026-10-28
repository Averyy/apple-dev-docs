# removeEntry(at:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Removes and releases the entry at the specified index.

**Availability**:
- macOS 10.0+ - Deprecated in 10.10

> **Deprecated**: Use NSTextField directly instead, and consider NSStackView for layout assistance

## Declaration

```swift
func removeEntry(at index: Int)
```

```objc
- (void) removeEntryAtIndex:(NSInteger) index;
```

## Discussion

If the specified index is invalid, this method does nothing.

## Parameters

- `index`: The zero-based index identifying the desired entry.

## See Also

### Adding and Removing Entries
- [func addEntry(String) -> NSFormCell](./addentry%28_%29.md)
  Adds a new entry to the end of the receiver and gives it the specified title.
- [func insertEntry(String, at: Int) -> NSFormCell!](./insertentry%28_,at%29.md)
  Inserts an entry with the specified title into the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsform/removeentry(at:))*