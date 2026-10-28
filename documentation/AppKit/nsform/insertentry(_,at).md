# insertEntry(_:at:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Inserts an entry with the specified title into the receiver.

**Availability**:
- macOS 10.0+ - Deprecated in 10.10

> **Deprecated**: Use NSTextField directly instead, and consider NSStackView for layout assistance

## Declaration

```swift
func insertEntry(_ title: String, at index: Int) -> NSFormCell!
```

```objc
- (NSFormCell *) insertEntry:(NSString *) title atIndex:(NSInteger) index;
```

## Return Value

The form cell object that was created for the entry.

## Discussion

The new entry has no tag, target, or action, but is enabled and editable.

## Parameters

- `title`: The title for the new form entry.
- `index`: The zero-based index at which to insert the entry.

## See Also

### Adding and Removing Entries
- [func addEntry(String) -> NSFormCell](./addentry%28_%29.md)
  Adds a new entry to the end of the receiver and gives it the specified title.
- [func removeEntry(at: Int)](./removeentry%28at%29.md)
  Removes and releases the entry at the specified index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsform/insertentry(_:at:))*