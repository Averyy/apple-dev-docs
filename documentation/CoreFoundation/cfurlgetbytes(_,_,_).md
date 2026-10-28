# CFURLGetBytes(_:_:_:)

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Returns by reference the byte representation of a URL object.

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
func CFURLGetBytes(_ url: CFURL!, _ buffer: UnsafeMutablePointer<UInt8>!, _ bufferLength: CFIndex) -> CFIndex
```

```c
extern CFIndex CFURLGetBytes(CFURLRef url, UInt8 *buffer, CFIndex bufferLength);
```

## Return Value

Returns the number of bytes in `buffer` that were filled. If the buffer is of insufficient size, returns `-1`.

## Parameters

- `url`: The URL object to convert to a byte representation.
- `buffer`: The buffer where you want the bytes to be placed. If the buffer is of insufficient size, returns `-1` and no bytes are placed in buffer. If `NULL` the needed length is computed and returned. The returned bytes are the original bytes from which the URL was created (*not* including the base URL). If the URL was created from a string, the bytes are the bytes of the string encoded via UTF-8.
- `bufferLength`: The number of bytes in `buffer`.

## See Also

### Getting URL Properties
- [func CFURLGetBaseURL(CFURL!) -> CFURL!](./cfurlgetbaseurl%28_%29.md)
  Returns the base URL of a given URL if it exists.
- [func CFURLGetByteRangeForComponent(CFURL!, CFURLComponentType, UnsafeMutablePointer<CFRange>!) -> CFRange](./cfurlgetbyterangeforcomponent%28_,_,_%29.md)
  Returns the range of the specified component in the bytes of a URL.
- [func CFURLGetTypeID() -> CFTypeID](./cfurlgettypeid%28%29.md)
  Returns the type identifier for the `CFURL` opaque type.
- [func CFURLResourceIsReachable(CFURL!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](./cfurlresourceisreachable%28_,_%29.md)
  Returns whether the resource pointed to by a file URL can be reached.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfurlgetbytes(_:_:_:))*