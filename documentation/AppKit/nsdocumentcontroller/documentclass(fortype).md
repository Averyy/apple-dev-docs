# documentClass(forType:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns the `NSDocument` subclass associated with a given document type.

**Availability**:
- macOS

## Declaration

```swift
func documentClass(forType typeName: String) -> AnyClass?
```

```objc
- (Class) documentClassForType:(NSString *) typeName;
```

## Return Value

Returns the `NSDocument` subclass associated with `documentTypeName`. If the class cannot be found, returns `nil`.

## Parameters

- `typeName`: The name of a document type, specified by `CFBundleTypeName` in the application’s `Info.plist` file.

  The document type must be one the receiver can read.

## See Also

### Managing Document Types
- [var documentClassNames: [String]](./documentclassnames.md)
  An array of strings representing the custom document classes supported by this app.
- [var defaultType: String?](./defaulttype.md)
  Returns the name of the document type that should be used when creating new documents.
- [func displayName(forType: String) -> String?](./displayname%28fortype%29.md)
  Returns the descriptive name for the specified document type, which is used in the File Format pop-up menu of the Save As dialog.
- [func typeForContents(of: URL) throws -> String](./typeforcontents%28of%29.md)
  Returns, for a specified URL, the document type identifier to use when opening the document at that location, if successful.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocumentcontroller/documentclass(fortype:))*