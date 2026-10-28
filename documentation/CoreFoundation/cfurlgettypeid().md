# CFURLGetTypeID()

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Returns the type identifier for the `CFURL` opaque type.

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
func CFURLGetTypeID() -> CFTypeID
```

```c
extern CFTypeID CFURLGetTypeID();
```

## Return Value

The type identifier for the `CFURL` opaque type.

## See Also

### Getting URL Properties
- [func CFURLGetBaseURL(CFURL!) -> CFURL!](./cfurlgetbaseurl%28_%29.md)
  Returns the base URL of a given URL if it exists.
- [func CFURLGetBytes(CFURL!, UnsafeMutablePointer<UInt8>!, CFIndex) -> CFIndex](./cfurlgetbytes%28_,_,_%29.md)
  Returns by reference the byte representation of a URL object.
- [func CFURLGetByteRangeForComponent(CFURL!, CFURLComponentType, UnsafeMutablePointer<CFRange>!) -> CFRange](./cfurlgetbyterangeforcomponent%28_,_,_%29.md)
  Returns the range of the specified component in the bytes of a URL.
- [func CFURLResourceIsReachable(CFURL!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](./cfurlresourceisreachable%28_,_%29.md)
  Returns whether the resource pointed to by a file URL can be reached.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfurlgettypeid())*