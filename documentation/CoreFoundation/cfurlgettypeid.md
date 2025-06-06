# CFURLGetTypeID()

**Framework**: Core Foundation  
**Kind**: func

Returns the type identifier for the `CFURL` opaque type.

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
func CFURLGetTypeID() -> CFTypeID
```

#### Return Value

The type identifier for the `CFURL` opaque type.

## See Also

- [func CFURLGetBaseURL(CFURL!) -> CFURL!](cfurlgetbaseurl(_:).md)
  Returns the base URL of a given URL if it exists.
- [func CFURLGetBytes(CFURL!, UnsafeMutablePointer<UInt8>!, CFIndex) -> CFIndex](cfurlgetbytes(_:_:_:).md)
  Returns by reference the byte representation of a URL object.
- [func CFURLGetByteRangeForComponent(CFURL!, CFURLComponentType, UnsafeMutablePointer<CFRange>!) -> CFRange](cfurlgetbyterangeforcomponent(_:_:_:).md)
  Returns the range of the specified component in the bytes of a URL.
- [func CFURLResourceIsReachable(CFURL!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](cfurlresourceisreachable(_:_:).md)
  Returns whether the resource pointed to by a file URL can be reached.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfurlgettypeid())*