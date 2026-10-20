# isNativeType(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Type Method

Returns a Boolean value that indicates whether the document can read and write the data natively.

**Availability**:
- macOS

## Declaration

```swift
class func isNativeType(_ type: String) -> Bool
```

```objc
+ (BOOL) isNativeType:(NSString *) type;
```

#### Return Value

[`true`](../../Swift/true.md) if the document type is a native type; otherwise, [`false`](../../Swift/false.md).

## Parameters

- `type`: The string that identifies the document type to test.

## See Also

### Managing File Type Information
- [class var readableTypes: [String]](./readabletypes.md)
  Returns the types of data the receiver can read natively and any types filterable to that native type.
- [class var writableTypes: [String]](./writabletypes.md)
  Returns the types of data the receiver can write natively and any types filterable to that native type.
- [func writableTypes(for: NSDocument.SaveOperationType) -> [String]](./writabletypes%28for%29.md)
  Returns the names of the types to which this document can be saved for a specified kind of save operation.
- [func fileNameExtension(forType: String, saveOperation: NSDocument.SaveOperationType) -> String?](./filenameextension%28fortype,saveoperation%29.md)
  Returns a filename extension that can be appended to a base filename, for a specified file type and kind of save operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocument/isnativetype(_:))*