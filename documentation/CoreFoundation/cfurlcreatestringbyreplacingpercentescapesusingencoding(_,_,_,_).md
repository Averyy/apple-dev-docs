# CFURLCreateStringByReplacingPercentEscapesUsingEncoding(_:_:_:_:)

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Creates a new string by replacing any percent escape sequences with their character equivalent.

**Availability**:
- iOS 2.0+ - Deprecated in 9.0
- iPadOS 2.0+ - Deprecated in 9.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.0+ - Deprecated in 10.11
- tvOS 9.0+ - Deprecated in 9.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 2.0+ - Deprecated in 2.0

> **Deprecated**: Use [NSString stringByRemovingPercentEncoding] or CFURLCreateStringByReplacingPercentEscapes() instead, which always uses the recommended UTF-8 encoding.

## Declaration

```swift
func CFURLCreateStringByReplacingPercentEscapesUsingEncoding(_ allocator: CFAllocator!, _ origString: CFString!, _ charsToLeaveEscaped: CFString!, _ encoding: CFStringEncoding) -> CFString!
```

```c
extern CFStringRefCFURLCreateStringByReplacingPercentEscapesUsingEncoding(CFAllocatorRef allocator, CFStringRef origString, CFStringRef charsToLeaveEscaped, CFStringEncoding encoding);
```

## Return Value

A new `CFString` object, or `NULL` if the percent escapes cannot be converted to characters, assuming the encoding given by `encoding`. If no characters need to be replaced, this function returns the original string with its reference count incremented. Ownership follows the create rule. See [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## Parameters

- `allocator`: The allocator to use to allocate memory for the new `CFString` object. Pass `NULL` or [`kCFAllocatorDefault`](./kcfallocatordefault.md) to use the current default allocator.
- `origString`: The `CFString` object to be copied and modified.
- `charsToLeaveEscaped`: Characters whose percent escape sequences, such as `%20` for a space character, you want to leave intact. Pass `NULL` to specify that no percent escapes be replaced, or the empty string (`CFSTR("")`) to specify that all be replaced.
- `encoding`: Specifies the encoding to use when interpreting percent escapes. If you are uncertain of the correct encoding, you should use UTF-8 ([`CFStringBuiltInEncodings.UTF8`](./cfstringbuiltinencodings/utf8.md)), which is the encoding designated by RFC 3986 as the correct encoding for use in URLs.

## See Also

### Converting URLs to Other Representations
- [func CFURLCreateData(CFAllocator!, CFURL!, CFStringEncoding, Bool) -> CFData!](./cfurlcreatedata%28_,_,_,_%29.md)
  Creates a `CFData` object containing the content of a given URL.
- [func CFURLCreateStringByAddingPercentEscapes(CFAllocator!, CFString!, CFString!, CFString!, CFStringEncoding) -> CFString!](./cfurlcreatestringbyaddingpercentescapes%28_,_,_,_,_%29.md)
  Creates a copy of a string, replacing certain characters with the equivalent percent escape sequence based on the specified encoding.
- [func CFURLCreateStringByReplacingPercentEscapes(CFAllocator!, CFString!, CFString!) -> CFString!](./cfurlcreatestringbyreplacingpercentescapes%28_,_,_%29.md)
  Creates a new string by replacing any percent escape sequences with their character equivalent.
- [func CFURLGetFileSystemRepresentation(CFURL!, Bool, UnsafeMutablePointer<UInt8>!, CFIndex) -> Bool](./cfurlgetfilesystemrepresentation%28_,_,_,_%29.md)
  Fills a buffer with the file system’s native string representation of a given URL’s path.
- [func CFURLGetFSRef(CFURL!, OpaquePointer!) -> Bool](./cfurlgetfsref%28_,_%29.md)
  Converts a given URL to a file or directory object.
- [func CFURLGetString(CFURL!) -> CFString!](./cfurlgetstring%28_%29.md)
  Returns the URL as a `CFString` object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfurlcreatestringbyreplacingpercentescapesusingencoding(_:_:_:_:))*