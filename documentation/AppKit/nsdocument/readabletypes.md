# readableTypes

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

Returns the types of data the receiver can read natively and any types filterable to that native type.

**Availability**:
- macOS

## Declaration

```swift
class var readableTypes: [String] { get }
```

```objc
@property (class, copy, readonly) NSArray<NSString *> * readableTypes;
```

## Return Value

An array of `NSString` objects representing the readable document types.

## See Also

### Related Documentation
- [class func canConcurrentlyReadDocuments(ofType: String) -> Bool](./canconcurrentlyreaddocuments%28oftype%29.md)
  Returns a Boolean value that indicates whether the receiver reads multiple documents of the given type concurrently.
### Managing File Type Information
- [class var writableTypes: [String]](./writabletypes.md)
  Returns the types of data the receiver can write natively and any types filterable to that native type.
- [class func isNativeType(String) -> Bool](./isnativetype%28_%29.md)
  Returns a Boolean value that indicates whether the document can read and write the data natively.
- [func writableTypes(for: NSDocument.SaveOperationType) -> [String]](./writabletypes%28for%29.md)
  Returns the names of the types to which this document can be saved for a specified kind of save operation.
- [func fileNameExtension(forType: String, saveOperation: NSDocument.SaveOperationType) -> String?](./filenameextension%28fortype,saveoperation%29.md)
  Returns a filename extension that can be appended to a base filename, for a specified file type and kind of save operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocument/readabletypes)*