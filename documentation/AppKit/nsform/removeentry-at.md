# removeEntry(at:)

**Framework**: AppKit  
**Kind**: method

Removes and releases the entry at the specified index.

**Availability**:
- macOS 10.0+

## Declaration

```swift
@MainActor
func removeEntry(at index: Int)
```

#### Discussion

If the specified index is invalid, this method does nothing.

## Parameters

- `index`: The zero-based index identifying the desired entry.

## See Also

- [func addEntry(String) -> NSFormCell](nsform/addentry(_:).md)
  Adds a new entry to the end of the receiver and gives it the specified title.
- [func insertEntry(String, at: Int) -> NSFormCell!](nsform/insertentry(_:at:).md)
  Inserts an entry with the specified title into the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsform/removeentry(at:))*