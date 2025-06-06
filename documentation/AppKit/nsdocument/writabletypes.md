# writableTypes

**Framework**: AppKit  
**Kind**: property

Returns the types of data the receiver can write natively and any types filterable to that native type.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
class var writableTypes: [String] { get }
```

#### Return Value

An array of `NSString` objects representing the writable document types.

## See Also

- [class var readableTypes: [String]](nsdocument/readabletypes.md)
  Returns the types of data the receiver can read natively and any types filterable to that native type.
- [class func isNativeType(String) -> Bool](nsdocument/isnativetype(_:).md)
  Returns a Boolean value that indicates whether the document can read and write the data natively.
- [func writableTypes(for: NSDocument.SaveOperationType) -> [String]](nsdocument/writabletypes(for:).md)
  Returns the names of the types to which this document can be saved for a specified kind of save operation.
- [func fileNameExtension(forType: String, saveOperation: NSDocument.SaveOperationType) -> String?](nsdocument/filenameextension(fortype:saveoperation:).md)
  Returns a filename extension that can be appended to a base filename, for a specified file type and kind of save operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocument/writabletypes)*