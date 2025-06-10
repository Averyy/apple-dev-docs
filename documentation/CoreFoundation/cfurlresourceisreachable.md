# CFURLResourceIsReachable(_:_:)

**Framework**: Core Foundation  
**Kind**: func

Returns whether the resource pointed to by a file URL can be reached.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.6+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func CFURLResourceIsReachable(_ url: CFURL!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool
```

#### Return Value

`true` if the resource is reachable; otherwise,  `false`.

#### Discussion

This function synchronously checks if the file at the provided URL is reachable. Checking reachability is appropriate when making decisions that do not require other immediate operations on the resource, such as periodic maintenance of user interface state that depends on the existence of a specific document. For example, you might remove an item from a download list if the user deletes the file.

If your app must perform operations on the file, such as opening it or copying resource properties, it is more efficient to attempt the operation and handle any failure that may occur.

If this function returns `false`, the object pointer referenced by `error` is populated with additional information.

> **Note**:  This method is currently applicable only to URLs for file system resources. For other URL types, this method always returns `false`.

## Parameters

- `url`: The URL to check.
- `error`: The error that occurred when the resource could not be reached.

## See Also

- [func CFURLGetBaseURL(CFURL!) -> CFURL!](cfurlgetbaseurl(_:).md)
  Returns the base URL of a given URL if it exists.
- [func CFURLGetBytes(CFURL!, UnsafeMutablePointer<UInt8>!, CFIndex) -> CFIndex](cfurlgetbytes(_:_:_:).md)
  Returns by reference the byte representation of a URL object.
- [func CFURLGetByteRangeForComponent(CFURL!, CFURLComponentType, UnsafeMutablePointer<CFRange>!) -> CFRange](cfurlgetbyterangeforcomponent(_:_:_:).md)
  Returns the range of the specified component in the bytes of a URL.
- [func CFURLGetTypeID() -> CFTypeID](cfurlgettypeid().md)
  Returns the type identifier for the `CFURL` opaque type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfurlresourceisreachable(_:_:))*