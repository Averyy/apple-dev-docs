# comment

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

The cookie’s comment string.

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
var comment: String? { get }
```

```objc
@property (copy, readonly, nullable) NSString * comment;
```

#### Discussion

This value is `nil` if the cookie has no comment. You can present this string to the user, explaining the contents and purpose of this cookie.

## See Also

### Getting user-readable cookie metadata
- [var commentURL: URL?](./commenturl.md)
  The cookie’s comment URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/httpcookie/comment)*