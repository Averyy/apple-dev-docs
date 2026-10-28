# CFURLGetFSRef(_:_:)

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Converts a given URL to a file or directory object.

**Availability**:
- iOS 2.0+ - Deprecated in 7.0
- iPadOS 2.0+ - Deprecated in 7.0
- Mac Catalyst 2.0+ - Deprecated in 7.0
- tvOS 9.0+ - Deprecated in 9.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 2.0+ - Deprecated in 2.0

> **Deprecated**: Not supported

## Declaration

```swift
func CFURLGetFSRef(_ url: CFURL!, _ fsRef: OpaquePointer!) -> Bool
```

```c
extern Boolean CFURLGetFSRef(CFURLRef url, struct FSRef *fsRef);
```

## Return Value

`true` if the conversion was successful, otherwise `false`.

## Discussion

The function cannot create an `FSRef` object if any of the leading path parts specified by `url` is an alias. The function can, however, traverse symbolic links.

## Parameters

- `url`: The `CFURL` object to convert to a file or directory object.
- `fsRef`: Upon return, contains the file or directory object representing `url`.

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
- [func CFURLGetFileSystemRepresentation(CFURL!, Bool, UnsafeMutablePointer<UInt8>!, CFIndex) -> Bool](./cfurlgetfilesystemrepresentation%28_,_,_,_%29.md)
  Fills a buffer with the file system’s native string representation of a given URL’s path.
- [func CFURLGetString(CFURL!) -> CFString!](./cfurlgetstring%28_%29.md)
  Returns the URL as a `CFString` object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfurlgetfsref(_:_:))*