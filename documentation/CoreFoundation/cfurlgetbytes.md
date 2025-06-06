# CFURLGetBytes(_:_:_:)

**Framework**: Core Foundation  
**Kind**: func

Returns by reference the byte representation of a URL object.

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
func CFURLGetBytes(_ url: CFURL!, _ buffer: UnsafeMutablePointer<UInt8>!, _ bufferLength: CFIndex) -> CFIndex
```

#### Return Value

Returns the number of bytes in `buffer` that were filled. If the buffer is of insufficient size, returns `-1`.

## Parameters

- `url`: The URL object to convert to a byte representation.
- `buffer`: The buffer where you want the bytes to be placed. If the buffer is of insufficient size, returns   and no bytes are placed in buffer. If   the needed length is computed and returned. The returned bytes are the original bytes from which the URL was created (  including the base URL). If the URL was created from a string, the bytes are the bytes of the string encoded via UTF-8.
- `bufferLength`: The number of bytes in  .

## See Also

- [func CFURLGetBaseURL(CFURL!) -> CFURL!](cfurlgetbaseurl(_:).md)
  Returns the base URL of a given URL if it exists.
- [func CFURLGetByteRangeForComponent(CFURL!, CFURLComponentType, UnsafeMutablePointer<CFRange>!) -> CFRange](cfurlgetbyterangeforcomponent(_:_:_:).md)
  Returns the range of the specified component in the bytes of a URL.
- [func CFURLGetTypeID() -> CFTypeID](cfurlgettypeid().md)
  Returns the type identifier for the `CFURL` opaque type.
- [func CFURLResourceIsReachable(CFURL!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](cfurlresourceisreachable(_:_:).md)
  Returns whether the resource pointed to by a file URL can be reached.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfurlgetbytes(_:_:_:))*