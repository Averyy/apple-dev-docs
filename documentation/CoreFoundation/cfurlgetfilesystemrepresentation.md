# CFURLGetFileSystemRepresentation(_:_:_:_:)

**Framework**: Core Foundation  
**Kind**: func

Fills a buffer with the file system’s native string representation of a given URL’s path.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
func CFURLGetFileSystemRepresentation(_ url: CFURL!, _ resolveAgainstBase: Bool, _ buffer: UnsafeMutablePointer<UInt8>!, _ maxBufLen: CFIndex) -> Bool
```

#### Return Value

`true` if successful, `false` if an error occurred.

#### Discussion

No more than `maxBufLen` bytes are written to `buffer`. If `url` requires more than `maxBufLen` bytes to represent itself, including the terminating null byte, this function returns `false`. To avoid this possible failure, you should pass a buffer with size of at least the maximum path length for the file system in question.

## Parameters

- `url`: The   object whose native file system representation you want to obtain.
- `resolveAgainstBase`: Pass   to return an absolute path name.
- `buffer`: A pointer to a character buffer. On return, the buffer holds the native file system’s representation of  . The buffer is null-terminated. This parameter must be at least   in size for the file system in question to avoid failures for insufficiently large buffers.
- `maxBufLen`: The maximum number of characters that can be written to  .

## See Also

- [func CFURLCreateData(CFAllocator!, CFURL!, CFStringEncoding, Bool) -> CFData!](cfurlcreatedata(_:_:_:_:).md)
  Creates a `CFData` object containing the content of a given URL.
- [func CFURLCreateStringByAddingPercentEscapes(CFAllocator!, CFString!, CFString!, CFString!, CFStringEncoding) -> CFString!](cfurlcreatestringbyaddingpercentescapes(_:_:_:_:_:).md)
  Creates a copy of a string, replacing certain characters with the equivalent percent escape sequence based on the specified encoding.
- [func CFURLCreateStringByReplacingPercentEscapes(CFAllocator!, CFString!, CFString!) -> CFString!](cfurlcreatestringbyreplacingpercentescapes(_:_:_:).md)
  Creates a new string by replacing any percent escape sequences with their character equivalent.
- [func CFURLCreateStringByReplacingPercentEscapesUsingEncoding(CFAllocator!, CFString!, CFString!, CFStringEncoding) -> CFString!](cfurlcreatestringbyreplacingpercentescapesusingencoding(_:_:_:_:).md)
  Creates a new string by replacing any percent escape sequences with their character equivalent.
- [func CFURLGetFSRef(CFURL!, OpaquePointer!) -> Bool](cfurlgetfsref(_:_:).md)
  Converts a given URL to a file or directory object.
- [func CFURLGetString(CFURL!) -> CFString!](cfurlgetstring(_:).md)
  Returns the URL as a `CFString` object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfurlgetfilesystemrepresentation(_:_:_:_:))*