# fileNameExtension(forType:saveOperation:)

**Framework**: AppKit  
**Kind**: method

Returns a filename extension that can be appended to a base filename, for a specified file type and kind of save operation.

**Availability**:
- macOS 10.5+

## Declaration

```swift
nonisolated
func fileNameExtension(forType typeName: String, saveOperation: NSDocument.SaveOperationType) -> String?
```

#### Return Value

The filename extension.

#### Discussion

The default implementation of this method invokes [`preferredFilenameExtension(forType:)`](nsworkspace/preferredfilenameextension(fortype:).md) on the shared workspace object if the type is a UTI or, if it is not, for backward binary compatibility with OS X v10.4 and earlier, invokes [`fileExtensionsFromType:`](nsdocumentcontroller/fileextensionsfromtype:.md) on the shared document controller and chooses the first filename extension in the returned array.

You can override this method to customize the appending of extensions to filenames by `NSDocument`. Starting in OS X v10.5, it is invoked from only two places in AppKit:

1. The [`autosave(withDelegate:didAutosave:contextInfo:)`](nsdocument/autosave(withdelegate:didautosave:contextinfo:).md) method uses this method when creating a new filename for the autosaved contents.
2. The [`handleSave(_:)`](nsdocument/handlesave(_:).md) method uses this method when adding an extension to the filename specified by a script.

In all other cases, the name of any file being saved will have been fully specified by the user with the Save panel (whether they know it or not).

## Parameters

- `typeName`: The file type.
- `saveOperation`: The kind of save operation.

## See Also

- [class var readableTypes: [String]](nsdocument/readabletypes.md)
  Returns the types of data the receiver can read natively and any types filterable to that native type.
- [class var writableTypes: [String]](nsdocument/writabletypes.md)
  Returns the types of data the receiver can write natively and any types filterable to that native type.
- [class func isNativeType(String) -> Bool](nsdocument/isnativetype(_:).md)
  Returns a Boolean value that indicates whether the document can read and write the data natively.
- [func writableTypes(for: NSDocument.SaveOperationType) -> [String]](nsdocument/writabletypes(for:).md)
  Returns the names of the types to which this document can be saved for a specified kind of save operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocument/filenameextension(fortype:saveoperation:))*