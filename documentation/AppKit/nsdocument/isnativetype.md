# isNativeType(_:)

**Framework**: AppKit  
**Kind**: method

Returns a Boolean value that indicates whether the document can read and write the data natively.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
class func isNativeType(_ type: String) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if the document type is a native type; otherwise, [`false`](https://developer.apple.com/documentation/Swift/false).

## Parameters

- `type`: The string that identifies the document type to test.

## See Also

- [class var readableTypes: [String]](nsdocument/readabletypes.md)
  Returns the types of data the receiver can read natively and any types filterable to that native type.
- [class var writableTypes: [String]](nsdocument/writabletypes.md)
  Returns the types of data the receiver can write natively and any types filterable to that native type.
- [func writableTypes(for: NSDocument.SaveOperationType) -> [String]](nsdocument/writabletypes(for:).md)
  Returns the names of the types to which this document can be saved for a specified kind of save operation.
- [func fileNameExtension(forType: String, saveOperation: NSDocument.SaveOperationType) -> String?](nsdocument/filenameextension(fortype:saveoperation:).md)
  Returns a filename extension that can be appended to a base filename, for a specified file type and kind of save operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocument/isnativetype(_:))*