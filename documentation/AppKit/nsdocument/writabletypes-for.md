# writableTypes(for:)

**Framework**: AppKit  
**Kind**: method

Returns the names of the types to which this document can be saved for a specified kind of save operation.

**Availability**:
- macOS ?+

## Declaration

```swift
nonisolated
func writableTypes(for saveOperation: NSDocument.SaveOperationType) -> [String]
```

#### Return Value

An array of `NSString` objects representing the writable document types.

#### Discussion

The save operation type is represented by `saveOperation`. For every kind of save operation except `NSSaveToOperation`, the returned array must only include types for which the app can play the Editor role. For `NSSaveToOperation` the returned array may include types for which the app can only play the Viewer role, and other types that the app can merely export. The default implementation of this method returns `[[self class] writableTypes]` with, except during `NSSaveToOperation`, types for which [`isNativeType(_:)`](nsdocument/isnativetype(_:).md) returns [`false`](https://developer.apple.com/documentation/Swift/false) filtered out.

You can override this method to limit the set of writable types when the document currently contains data that is not representable in all types. For example, you can disallow saving to RTF files when the document contains an attachment and can only be saved properly to RTFD files.

You can invoke this method when creating a custom save panel accessory view to present easily the same set of types as `NSDocument` does in its standard file format popup menu.

## Parameters

- `saveOperation`: The kind of save operation.

## See Also

- [class var readableTypes: [String]](nsdocument/readabletypes.md)
  Returns the types of data the receiver can read natively and any types filterable to that native type.
- [class var writableTypes: [String]](nsdocument/writabletypes.md)
  Returns the types of data the receiver can write natively and any types filterable to that native type.
- [class func isNativeType(String) -> Bool](nsdocument/isnativetype(_:).md)
  Returns a Boolean value that indicates whether the document can read and write the data natively.
- [func fileNameExtension(forType: String, saveOperation: NSDocument.SaveOperationType) -> String?](nsdocument/filenameextension(fortype:saveoperation:).md)
  Returns a filename extension that can be appended to a base filename, for a specified file type and kind of save operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocument/writabletypes(for:))*