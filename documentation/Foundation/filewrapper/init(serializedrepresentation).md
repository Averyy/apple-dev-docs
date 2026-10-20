# init(serializedRepresentation:)

**Framework**: Foundation  
**Kind**: init  
**Role**: Initializer

Initializes the receiver as a regular-file file wrapper from given serialized data.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
init?(serializedRepresentation serializeRepresentation: Data)
```

```objc
- (instancetype) initWithSerializedRepresentation:(NSData *) serializeRepresentation;
```

#### Return Value

Regular-file file wrapper initialized from `serializedRepresentation`.

#### Discussion

The file wrapper is not associated with a file-system node until you save it using [`write(to:options:originalContentsURL:)`](./write%28to,options,originalcontentsurl%29.md).

## Parameters

- `serializeRepresentation`: Serialized representation of a file wrapper in the format used for the `NSFileContentsPboardType` pasteboard type. Data of this format is returned by such methods as [`serializedRepresentation`](./serializedrepresentation.md) and [`rtfd(from:documentAttributes:)`](../nsattributedstring/rtfd%28from,documentattributes%29.md) ([`NSAttributedString`](../nsattributedstring.md)).

## See Also

### Related Documentation
- [var preferredFilename: String?](./preferredfilename.md)
  The preferred filename for the file wrapper object.
- [var filename: String?](./filename.md)
  The filename of the file wrapper object
- [var fileAttributes: [String : Any]](./fileattributes.md)
  A dictionary of file attributes.
### Creating File Wrappers
- [init(url: URL, options: FileWrapper.ReadingOptions) throws](./init%28url,options%29-70161.md)
  Initializes a file wrapper instance whose kind is determined by the type of file-system node located by the URL.
- [convenience init?(path: String)](./init%28path%29.md)
  Initializes a file wrapper instance whose kind is determined by the type of file-system node located by the path.
- [init(directoryWithFileWrappers: [String : FileWrapper])](./init%28directorywithfilewrappers%29.md)
  Initializes the receiver as a directory file wrapper, with a given file-wrapper list.
- [init(regularFileWithContents: Data)](./init%28regularfilewithcontents%29.md)
  Initializes the receiver as a regular-file file wrapper.
- [convenience init(symbolicLinkWithDestination: String)](./init%28symboliclinkwithdestination%29.md)
  Initializes the receiver as a symbolic-link file wrapper.
- [init(symbolicLinkWithDestinationURL: URL)](./init%28symboliclinkwithdestinationurl%29.md)
  Initializes the receiver as a symbolic-link file wrapper that links to a specified file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/filewrapper/init(serializedrepresentation:))*