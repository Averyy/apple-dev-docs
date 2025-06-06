# CFURLCreateData(_:_:_:_:)

**Framework**: Core Foundation  
**Kind**: func

Creates a `CFData` object containing the content of a given URL.

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
func CFURLCreateData(_ allocator: CFAllocator!, _ url: CFURL!, _ encoding: CFStringEncoding, _ escapeWhitespace: Bool) -> CFData!
```

#### Return Value

A new `CFData` object containing the content of `url`. Ownership follows the create rule. See [`The Create Rule`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

#### Discussion

This function escapes any character that is not 7-bit ASCII with the byte-code for the given encoding. If `escapeWhitespace` is `true`, whitespace characters (’ ’, ‘\t’, ‘\r’, ‘\n’) will be escaped as well. This is desirable if you want to embed the URL into a larger text stream like HTML.

## Parameters

- `allocator`: The allocator to use to allocate memory for the new   object. Pass   or   to use the current default allocator.
- `url`: The URL to convert into a   object.
- `encoding`: The string encoding to use when converting   into a   object.
- `escapeWhitespace`:   if you want to escape whitespace characters in the URL,   otherwise.

## See Also

- [func CFURLCreateStringByAddingPercentEscapes(CFAllocator!, CFString!, CFString!, CFString!, CFStringEncoding) -> CFString!](cfurlcreatestringbyaddingpercentescapes(_:_:_:_:_:).md)
  Creates a copy of a string, replacing certain characters with the equivalent percent escape sequence based on the specified encoding.
- [func CFURLCreateStringByReplacingPercentEscapes(CFAllocator!, CFString!, CFString!) -> CFString!](cfurlcreatestringbyreplacingpercentescapes(_:_:_:).md)
  Creates a new string by replacing any percent escape sequences with their character equivalent.
- [func CFURLCreateStringByReplacingPercentEscapesUsingEncoding(CFAllocator!, CFString!, CFString!, CFStringEncoding) -> CFString!](cfurlcreatestringbyreplacingpercentescapesusingencoding(_:_:_:_:).md)
  Creates a new string by replacing any percent escape sequences with their character equivalent.
- [func CFURLGetFileSystemRepresentation(CFURL!, Bool, UnsafeMutablePointer<UInt8>!, CFIndex) -> Bool](cfurlgetfilesystemrepresentation(_:_:_:_:).md)
  Fills a buffer with the file system’s native string representation of a given URL’s path.
- [func CFURLGetFSRef(CFURL!, OpaquePointer!) -> Bool](cfurlgetfsref(_:_:).md)
  Converts a given URL to a file or directory object.
- [func CFURLGetString(CFURL!) -> CFString!](cfurlgetstring(_:).md)
  Returns the URL as a `CFString` object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfurlcreatedata(_:_:_:_:))*