# version

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

The cookie’s version.

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
var version: Int { get }
```

```objc
@property (readonly) NSUInteger version;
```

## Discussion

Version 0 maps to “old-style” Netscape cookies. Version 1 maps to [RFC 6265](https://tools.ietf.org/html/rfc6265) cookies.

## See Also

### Getting cookie metadata
- [var name: String](./name.md)
  The cookie’s name.
- [var value: String](./value.md)
  The cookie’s string value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/httpcookie/version)*