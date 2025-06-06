# defaultType

**Framework**: AppKit  
**Kind**: property

Returns the name of the document type that should be used when creating new documents.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var defaultType: String? { get }
```

#### Discussion

The default implementation of this method returns the first Editor type declared by the `CFBundleDocumentTypes` array in the application’s `Info.plist`, or returns `nil` if no Editor type is declared. You can override it to customize the type of document that is created when, for instance, the user chooses New in the File menu.

## See Also

- [var documentClassNames: [String]](nsdocumentcontroller/documentclassnames.md)
  An array of strings representing the custom document classes supported by this app.
- [func documentClass(forType: String) -> AnyClass?](nsdocumentcontroller/documentclass(fortype:).md)
  Returns the `NSDocument` subclass associated with a given document type.
- [func displayName(forType: String) -> String?](nsdocumentcontroller/displayname(fortype:).md)
  Returns the descriptive name for the specified document type, which is used in the File Format pop-up menu of the Save As dialog.
- [func typeForContents(of: URL) throws -> String](nsdocumentcontroller/typeforcontents(of:).md)
  Returns, for a specified URL, the document type identifier to use when opening the document at that location, if successful.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocumentcontroller/defaulttype)*