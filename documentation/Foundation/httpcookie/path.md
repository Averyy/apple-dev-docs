# path

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

The cookie’s path.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.2+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var path: String { get }
```

```objc
@property (copy, readonly) NSString * path;
```

## Discussion

The cookie will be sent with requests for this path in the cookie’s domain, and all paths that have this prefix. A path of `"/"` means the cookie will be sent for all URLs in the domain.

## See Also

### Getting cookie host properties
- [var domain: String](./domain.md)
  The domain of the cookie.
- [var portList: [NSNumber]?](./portlist.md)
  The cookie’s port list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/httpcookie/path)*