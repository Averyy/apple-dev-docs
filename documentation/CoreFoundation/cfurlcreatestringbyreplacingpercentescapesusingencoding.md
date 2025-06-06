# CFURLCreateStringByReplacingPercentEscapesUsingEncoding(_:_:_:_:)

**Framework**: Core Foundation  
**Kind**: func

Creates a new string by replacing any percent escape sequences with their character equivalent.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func CFURLCreateStringByReplacingPercentEscapesUsingEncoding(_ allocator: CFAllocator!, _ origString: CFString!, _ charsToLeaveEscaped: CFString!, _ encoding: CFStringEncoding) -> CFString!
```

#### Return Value

A new `CFString` object, or `NULL` if the percent escapes cannot be converted to characters, assuming the encoding given by `encoding`. If no characters need to be replaced, this function returns the original string with its reference count incremented. Ownership follows the create rule. See [`The Create Rule`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## Parameters

- `allocator`: The allocator to use to allocate memory for the new   object. Pass   or   to use the current default allocator.
- `origString`: The   object to be copied and modified.
- `charsToLeaveEscaped`: Characters whose percent escape sequences, such as   for a space character, you want to leave intact. Pass   to specify that no percent escapes be replaced, or the empty string ( ) to specify that all be replaced.
- `encoding`: Specifies the encoding to use when interpreting percent escapes. If you are uncertain of the correct encoding, you should use UTF-8 ( ), which is the encoding designated by RFC 3986 as the correct encoding for use in URLs.

## See Also

- [func CFURLCreateData(CFAllocator!, CFURL!, CFStringEncoding, Bool) -> CFData!](cfurlcreatedata(_:_:_:_:).md)
  Creates a `CFData` object containing the content of a given URL.
- [func CFURLCreateStringByAddingPercentEscapes(CFAllocator!, CFString!, CFString!, CFString!, CFStringEncoding) -> CFString!](cfurlcreatestringbyaddingpercentescapes(_:_:_:_:_:).md)
  Creates a copy of a string, replacing certain characters with the equivalent percent escape sequence based on the specified encoding.
- [func CFURLCreateStringByReplacingPercentEscapes(CFAllocator!, CFString!, CFString!) -> CFString!](cfurlcreatestringbyreplacingpercentescapes(_:_:_:).md)
  Creates a new string by replacing any percent escape sequences with their character equivalent.
- [func CFURLGetFileSystemRepresentation(CFURL!, Bool, UnsafeMutablePointer<UInt8>!, CFIndex) -> Bool](cfurlgetfilesystemrepresentation(_:_:_:_:).md)
  Fills a buffer with the file system’s native string representation of a given URL’s path.
- [func CFURLGetFSRef(CFURL!, OpaquePointer!) -> Bool](cfurlgetfsref(_:_:).md)
  Converts a given URL to a file or directory object.
- [func CFURLGetString(CFURL!) -> CFString!](cfurlgetstring(_:).md)
  Returns the URL as a `CFString` object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfurlcreatestringbyreplacingpercentescapesusingencoding(_:_:_:_:))*