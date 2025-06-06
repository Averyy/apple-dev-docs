# CFURLCreateStringByAddingPercentEscapes(_:_:_:_:_:)

**Framework**: Core Foundation  
**Kind**: func

Creates a copy of a string, replacing certain characters with the equivalent percent escape sequence based on the specified encoding.

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
func CFURLCreateStringByAddingPercentEscapes(_ allocator: CFAllocator!, _ originalString: CFString!, _ charactersToLeaveUnescaped: CFString!, _ legalURLCharactersToBeEscaped: CFString!, _ encoding: CFStringEncoding) -> CFString!
```

#### Return Value

A copy of `originalString` replacing certain characters. If it does not need to be modified (no percent escape sequences are missing), this function may merely return `originalString` with its reference count incremented. Ownership follows the create rule. See [`The Create Rule`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

#### Discussion

The characters escaped are all characters that are not legal URL characters (based on RFC 2396), plus any characters in `legalURLCharactersToBeEscaped`, less any characters in `charactersToLeaveUnescaped`. To simply correct any non-URL characters in an otherwise correct URL string, pass `NULL` for the `allocator`, `charactersToLeaveEscaped`, and `legalURLCharactersToBeEscaped` parameters, and [`CFStringBuiltInEncodings.UTF8`](cfstringbuiltinencodings/utf8.md) as the `encoding` parameter.

It may be difficult to use this function to “clean up” unescaped or partially escaped URL strings where sequences are unpredictable and you cannot specify `charactersToLeaveUnescaped`. Instead, you can “pre-process” a URL string using [`CFURLCreateStringByReplacingPercentEscapesUsingEncoding(_:_:_:_:)`](cfurlcreatestringbyreplacingpercentescapesusingencoding(_:_:_:_:).md) then add the escape characters using [`CFURLCreateStringByAddingPercentEscapes(_:_:_:_:_:)`](cfurlcreatestringbyaddingpercentescapes(_:_:_:_:_:).md), as shown in the following code fragment.

```objc
CFStringRef originalURLString = CFSTR("http://online.store.com/storefront/?request=get-document&doi=10.1175%2F1520-0426(2005)014%3C1157:DODADSS%3E2.0.CO%3B2");
CFStringRef preprocessedString =
    CFURLCreateStringByReplacingPercentEscapesUsingEncoding(kCFAllocatorDefault, originalURLString, CFSTR(""), kCFStringEncodingUTF8);
CFStringRef urlString =
    CFURLCreateStringByAddingPercentEscapes(kCFAllocatorDefault, preprocessedString, NULL, NULL, kCFStringEncodingUTF8);
url = CFURLCreateWithString(kCFAllocatorDefault, urlString, NULL);
```

## Parameters

- `allocator`: The allocator to use to allocate memory for the new   object. Pass   or   to use the current default allocator.
- `originalString`: The   object to copy.
- `charactersToLeaveUnescaped`: Characters whose percent escape sequences you want to leave intact. Pass   to specify that all illegal characters be escaped.
- `legalURLCharactersToBeEscaped`: Legal characters to be escaped. Pass   to specify that no legal characters be replaced.
- `encoding`: The encoding to use for the translation. If you are uncertain of the correct encoding, you should use UTF-8 ( ), which is the encoding designated by RFC 2396 as the correct encoding for use in URLs.

## See Also

- [func CFURLCreateData(CFAllocator!, CFURL!, CFStringEncoding, Bool) -> CFData!](cfurlcreatedata(_:_:_:_:).md)
  Creates a `CFData` object containing the content of a given URL.
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

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfurlcreatestringbyaddingpercentescapes(_:_:_:_:_:))*