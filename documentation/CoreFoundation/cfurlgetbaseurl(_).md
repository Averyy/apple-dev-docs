# CFURLGetBaseURL(_:)

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Returns the base URL of a given URL if it exists.

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
func CFURLGetBaseURL(_ anURL: CFURL!) -> CFURL!
```

```c
extern CFURLRefCFURLGetBaseURL(CFURLRef anURL);
```

#### Return Value

A `CFURL` object representing the base URL of `anURL`. Ownership follows the get rule. See [The Get Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-SW1).

## Parameters

- `anURL`: The `CFURL` object to examine.

## See Also

### Getting URL Properties
- [func CFURLGetBytes(CFURL!, UnsafeMutablePointer<UInt8>!, CFIndex) -> CFIndex](./cfurlgetbytes%28_,_,_%29.md)
  Returns by reference the byte representation of a URL object.
- [func CFURLGetByteRangeForComponent(CFURL!, CFURLComponentType, UnsafeMutablePointer<CFRange>!) -> CFRange](./cfurlgetbyterangeforcomponent%28_,_,_%29.md)
  Returns the range of the specified component in the bytes of a URL.
- [func CFURLGetTypeID() -> CFTypeID](./cfurlgettypeid%28%29.md)
  Returns the type identifier for the `CFURL` opaque type.
- [func CFURLResourceIsReachable(CFURL!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](./cfurlresourceisreachable%28_,_%29.md)
  Returns whether the resource pointed to by a file URL can be reached.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfurlgetbaseurl(_:))*