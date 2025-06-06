# CFURLGetBaseURL(_:)

**Framework**: Core Foundation  
**Kind**: func

Returns the base URL of a given URL if it exists.

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
func CFURLGetBaseURL(_ anURL: CFURL!) -> CFURL!
```

#### Return Value

A `CFURL` object representing the base URL of `anURL`. Ownership follows the get rule. See [`The Get Rule`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-SW1).

## Parameters

- `anURL`: The   object to examine.

## See Also

- [func CFURLGetBytes(CFURL!, UnsafeMutablePointer<UInt8>!, CFIndex) -> CFIndex](cfurlgetbytes(_:_:_:).md)
  Returns by reference the byte representation of a URL object.
- [func CFURLGetByteRangeForComponent(CFURL!, CFURLComponentType, UnsafeMutablePointer<CFRange>!) -> CFRange](cfurlgetbyterangeforcomponent(_:_:_:).md)
  Returns the range of the specified component in the bytes of a URL.
- [func CFURLGetTypeID() -> CFTypeID](cfurlgettypeid().md)
  Returns the type identifier for the `CFURL` opaque type.
- [func CFURLResourceIsReachable(CFURL!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](cfurlresourceisreachable(_:_:).md)
  Returns whether the resource pointed to by a file URL can be reached.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfurlgetbaseurl(_:))*