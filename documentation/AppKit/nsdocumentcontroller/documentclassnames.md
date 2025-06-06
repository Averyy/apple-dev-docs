# documentClassNames

**Framework**: AppKit  
**Kind**: property

An array of strings representing the custom document classes supported by this app.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var documentClassNames: [String] { get }
```

#### Discussion

The items in the array are [`NSString`](https://developer.apple.com/documentation/Foundation/NSString) objects, each of which represents the name of a document subclasses supported by the app. The document class names are derived from the app’s `Info.plist`.  You can override this property and use it to return the names of document classes that are dynamically loaded from plugins.

## See Also

- [var defaultType: String?](nsdocumentcontroller/defaulttype.md)
  Returns the name of the document type that should be used when creating new documents.
- [func documentClass(forType: String) -> AnyClass?](nsdocumentcontroller/documentclass(fortype:).md)
  Returns the `NSDocument` subclass associated with a given document type.
- [func displayName(forType: String) -> String?](nsdocumentcontroller/displayname(fortype:).md)
  Returns the descriptive name for the specified document type, which is used in the File Format pop-up menu of the Save As dialog.
- [func typeForContents(of: URL) throws -> String](nsdocumentcontroller/typeforcontents(of:).md)
  Returns, for a specified URL, the document type identifier to use when opening the document at that location, if successful.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocumentcontroller/documentclassnames)*