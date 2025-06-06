# insertEntry(_:at:)

**Framework**: AppKit  
**Kind**: method

Inserts an entry with the specified title into the receiver.

**Availability**:
- macOS 10.0+

## Declaration

```swift
@MainActor
func insertEntry(_ title: String, at index: Int) -> NSFormCell!
```

#### Return Value

The form cell object that was created for the entry.

#### Discussion

The new entry has no tag, target, or action, but is enabled and editable.

## Parameters

- `title`: The title for the new form entry.
- `index`: The zero-based index at which to insert the entry.

## See Also

- [func addEntry(String) -> NSFormCell](nsform/addentry(_:).md)
  Adds a new entry to the end of the receiver and gives it the specified title.
- [func removeEntry(at: Int)](nsform/removeentry(at:).md)
  Removes and releases the entry at the specified index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsform/insertentry(_:at:))*