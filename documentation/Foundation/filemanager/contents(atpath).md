# contents(atPath:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Returns the contents of the file at the specified path.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func contents(atPath path: String) -> Data?
```

```objc
- (NSData *) contentsAtPath:(NSString *) path;
```

#### Return Value

An [`NSData`](../nsdata.md) object with the contents of the file. If `path` specifies a directory, or if some other error occurs, this method returns `nil`.

## Parameters

- `path`: The path of the file whose contents you want.

## See Also

### Related Documentation
- [func createFile(atPath: String, contents: Data?, attributes: [FileAttributeKey : Any]?) -> Bool](./createfile%28atpath,contents,attributes%29.md)
  Creates a file with the specified content and attributes at the given location.
### Getting and comparing file contents
- [func contentsEqual(atPath: String, andPath: String) -> Bool](./contentsequal%28atpath,andpath%29.md)
  Returns a Boolean value that indicates whether the files or directories in specified paths have the same contents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/filemanager/contents(atpath:))*