# CFURLGetFileSystemRepresentation(_:_:_:_:)

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Fills a buffer with the file system’s native string representation of a given URL’s path.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
func CFURLGetFileSystemRepresentation(_ url: CFURL!, _ resolveAgainstBase: Bool, _ buffer: UnsafeMutablePointer<UInt8>!, _ maxBufLen: CFIndex) -> Bool
```

```c
extern Boolean CFURLGetFileSystemRepresentation(CFURLRef url, Boolean resolveAgainstBase, UInt8 *buffer, CFIndex maxBufLen);
```

## Return Value

`true` if successful, `false` if an error occurred.

## Discussion

No more than `maxBufLen` bytes are written to `buffer`. If `url` requires more than `maxBufLen` bytes to represent itself, including the terminating null byte, this function returns `false`. To avoid this possible failure, you should pass a buffer with size of at least the maximum path length for the file system in question.

## Parameters

- `url`: The `CFURL` object whose native file system representation you want to obtain.
- `resolveAgainstBase`: Pass `true` to return an absolute path name.
- `buffer`: A pointer to a character buffer. On return, the buffer holds the native file system’s representation of `url`. The buffer is null-terminated. This parameter must be at least `maxBufLen` in size for the file system in question to avoid failures for insufficiently large buffers.
- `maxBufLen`: The maximum number of characters that can be written to `buffer`.

## See Also

### Converting URLs to Other Representations
- [func CFURLCreateData(CFAllocator!, CFURL!, CFStringEncoding, Bool) -> CFData!](./cfurlcreatedata%28_,_,_,_%29.md)
  Creates a `CFData` object containing the content of a given URL.
- [func CFURLCreateStringByAddingPercentEscapes(CFAllocator!, CFString!, CFString!, CFString!, CFStringEncoding) -> CFString!](./cfurlcreatestringbyaddingpercentescapes%28_,_,_,_,_%29.md)
  Creates a copy of a string, replacing certain characters with the equivalent percent escape sequence based on the specified encoding.
- [func CFURLCreateStringByReplacingPercentEscapes(CFAllocator!, CFString!, CFString!) -> CFString!](./cfurlcreatestringbyreplacingpercentescapes%28_,_,_%29.md)
  Creates a new string by replacing any percent escape sequences with their character equivalent.
- [func CFURLCreateStringByReplacingPercentEscapesUsingEncoding(CFAllocator!, CFString!, CFString!, CFStringEncoding) -> CFString!](./cfurlcreatestringbyreplacingpercentescapesusingencoding%28_,_,_,_%29.md)
  Creates a new string by replacing any percent escape sequences with their character equivalent.
- [func CFURLGetFSRef(CFURL!, OpaquePointer!) -> Bool](./cfurlgetfsref%28_,_%29.md)
  Converts a given URL to a file or directory object.
- [func CFURLGetString(CFURL!) -> CFString!](./cfurlgetstring%28_%29.md)
  Returns the URL as a `CFString` object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfurlgetfilesystemrepresentation(_:_:_:_:))*