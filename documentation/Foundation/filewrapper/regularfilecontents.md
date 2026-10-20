# regularFileContents

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

The contents of the file-system node associated with a regular-file file wrapper.

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
var regularFileContents: Data? { get }
```

```objc
@property (copy, readonly, nullable) NSData * regularFileContents;
```

#### Discussion

This property may contain `nil` if the user modifies the file after you call [`read(from:options:)`](./read%28from,options%29.md) or [`init(url:options:)`](./init%28url,options%29-70161.md) but before [`FileWrapper`](../filewrapper.md) has read the contents of the file. Use the [`immediate`](./readingoptions/immediate.md) reading option to reduce the likelihood of that problem.

##### Special Considerations

This property raises `NSInternalInconsistencyException` if the file wrapper object is not a regular-file file wrapper.

## See Also

### Related Documentation
- [func read(from: URL, options: FileWrapper.ReadingOptions) throws](./read%28from,options%29.md)
  Recursively rereads the entire contents of a file wrapper from the specified location on disk.
- [init(regularFileWithContents: Data)](./init%28regularfilewithcontents%29.md)
  Initializes the receiver as a regular-file file wrapper.
### Accessing Files
- [var filename: String?](./filename.md)
  The filename of the file wrapper object
- [var preferredFilename: String?](./preferredfilename.md)
  The preferred filename for the file wrapper object.
- [var fileAttributes: [String : Any]](./fileattributes.md)
  A dictionary of file attributes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/filewrapper/regularfilecontents)*