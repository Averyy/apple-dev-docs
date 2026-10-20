# init(symbolicLinkWithDestinationURL:)

**Framework**: Foundation  
**Kind**: init  
**Role**: Initializer

Initializes the receiver as a symbolic-link file wrapper that links to a specified file.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.6+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
init(symbolicLinkWithDestinationURL url: URL)
```

```objc
- (instancetype) initSymbolicLinkWithDestinationURL:(NSURL *) url;
```

#### Return Value

Initialized symbolic-link file wrapper referencing `url`.

#### Discussion

The file wrapper is not associated with a file-system node until you save it using [`write(to:options:originalContentsURL:)`](./write%28to,options,originalcontentsurl%29.md).

The file wrapper is initialized with open permissions: anyone can modify or read the file reference. .

## Parameters

- `url`: URL of the file the file wrapper is to reference.

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
- [init?(serializedRepresentation: Data)](./init%28serializedrepresentation%29.md)
  Initializes the receiver as a regular-file file wrapper from given serialized data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/filewrapper/init(symboliclinkwithdestinationurl:))*