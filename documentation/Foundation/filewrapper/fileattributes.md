# fileAttributes

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

A dictionary of file attributes.

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
var fileAttributes: [String : Any] { get set }
```

```objc
@property (copy) NSDictionary<NSString *,id> * fileAttributes;
```

#### Discussion

The file attributes’ dictionary is the same format as that returned by [`attributesOfItem(atPath:)`](../filemanager/attributesofitem%28atpath%29.md) (`NSFileManager`).

## See Also

### Accessing Files
- [var filename: String?](./filename.md)
  The filename of the file wrapper object
- [var preferredFilename: String?](./preferredfilename.md)
  The preferred filename for the file wrapper object.
- [var regularFileContents: Data?](./regularfilecontents.md)
  The contents of the file-system node associated with a regular-file file wrapper.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/filewrapper/fileattributes)*