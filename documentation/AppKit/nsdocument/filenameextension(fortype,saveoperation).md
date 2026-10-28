# fileNameExtension(forType:saveOperation:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns a filename extension that can be appended to a base filename, for a specified file type and kind of save operation.

**Availability**:
- macOS 10.5+

## Declaration

```swift
nonisolated
func fileNameExtension(forType typeName: String, saveOperation: NSDocument.SaveOperationType) -> String?
```

```objc
- (NSString *) fileNameExtensionForType:(NSString *) typeName saveOperation:(NSSaveOperationType) saveOperation;
```

## Return Value

The filename extension.

## Discussion

The default implementation of this method invokes [`preferredFilenameExtension(forType:)`](../nsworkspace/preferredfilenameextension%28fortype%29.md) on the shared workspace object if the type is a UTI or, if it is not, for backward binary compatibility with OS X v10.4 and earlier, invokes [`fileExtensionsFromType:`](../nsdocumentcontroller/fileextensionsfromtype_.md) on the shared document controller and chooses the first filename extension in the returned array.

You can override this method to customize the appending of extensions to filenames by `NSDocument`. Starting in OS X v10.5, it is invoked from only two places in AppKit:

1. The [`autosave(withDelegate:didAutosave:contextInfo:)`](./autosave%28withdelegate,didautosave,contextinfo%29.md) method uses this method when creating a new filename for the autosaved contents.
2. The [`handleSave(_:)`](./handlesave%28_%29.md) method uses this method when adding an extension to the filename specified by a script.

In all other cases, the name of any file being saved will have been fully specified by the user with the Save panel (whether they know it or not).

## Parameters

- `typeName`: The file type.
- `saveOperation`: The kind of save operation.

## See Also

### Managing File Type Information
- [class var readableTypes: [String]](./readabletypes.md)
  Returns the types of data the receiver can read natively and any types filterable to that native type.
- [class var writableTypes: [String]](./writabletypes.md)
  Returns the types of data the receiver can write natively and any types filterable to that native type.
- [class func isNativeType(String) -> Bool](./isnativetype%28_%29.md)
  Returns a Boolean value that indicates whether the document can read and write the data natively.
- [func writableTypes(for: NSDocument.SaveOperationType) -> [String]](./writabletypes%28for%29.md)
  Returns the names of the types to which this document can be saved for a specified kind of save operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocument/filenameextension(fortype:saveoperation:))*