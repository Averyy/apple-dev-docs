# documentClass(forType:)

**Framework**: AppKit  
**Kind**: method

Returns the `NSDocument` subclass associated with a given document type.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func documentClass(forType typeName: String) -> AnyClass?
```

#### Return Value

Returns the `NSDocument` subclass associated with `documentTypeName`. If the class cannot be found, returns `nil`.

## Parameters

- `typeName`: The document type must be one the receiver can read.

## See Also

- [var documentClassNames: [String]](nsdocumentcontroller/documentclassnames.md)
  An array of strings representing the custom document classes supported by this app.
- [var defaultType: String?](nsdocumentcontroller/defaulttype.md)
  Returns the name of the document type that should be used when creating new documents.
- [func displayName(forType: String) -> String?](nsdocumentcontroller/displayname(fortype:).md)
  Returns the descriptive name for the specified document type, which is used in the File Format pop-up menu of the Save As dialog.
- [func typeForContents(of: URL) throws -> String](nsdocumentcontroller/typeforcontents(of:).md)
  Returns, for a specified URL, the document type identifier to use when opening the document at that location, if successful.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocumentcontroller/documentclass(fortype:))*