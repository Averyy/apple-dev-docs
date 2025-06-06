# duplicate(_:)

**Framework**: AppKit  
**Kind**: method

Creates a copy of the receiving document in response to the user choosing Duplicate from the File menu.

**Availability**:
- macOS 10.7+

## Declaration

```swift
@IBAction
@MainActor func duplicate(_ sender: Any?)
```

#### Discussion

The default implementation of this method merely invokes `[self duplicateDocumentWithDelegate:nil didDuplicateSelector:NULL contextInfo:NULL]`.

## Parameters

- `sender`: The control sending the action message.

## See Also

- [func duplicate() throws -> NSDocument](nsdocument/duplicate.md)
  Creates a new document whose contents are the same as the receiver and returns an error object if unsuccessful.
- [func duplicate(withDelegate: Any?, didDuplicate: Selector?, contextInfo: UnsafeMutableRawPointer?)](nsdocument/duplicate(withdelegate:didduplicate:contextinfo:).md)
  Creates a new document whose contents are the same as the current document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocument/duplicate(_:))*