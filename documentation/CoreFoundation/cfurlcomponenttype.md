# CFURLComponentType

**Framework**: Core Foundation  
**Kind**: enum

The types of components in a URL.

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
enum CFURLComponentType
```

#### Overview

These constants are used by the [`CFURLGetByteRangeForComponent(_:_:_:)`](cfurlgetbyterangeforcomponent(_:_:_:).md) function.

## Topics

### Constants
- [CFURLComponentType.scheme](cfurlcomponenttype/scheme.md)
  The URL’s scheme.
- [CFURLComponentType.netLocation](cfurlcomponenttype/netlocation.md)
  The URL’s network location.
- [CFURLComponentType.path](cfurlcomponenttype/path.md)
  The URL’s path component.
- [CFURLComponentType.resourceSpecifier](cfurlcomponenttype/resourcespecifier.md)
  The URL’s resource specifier.
- [CFURLComponentType.user](cfurlcomponenttype/user.md)
  The URL’s user.
- [CFURLComponentType.password](cfurlcomponenttype/password.md)
  The user’s password.
- [CFURLComponentType.userInfo](cfurlcomponenttype/userinfo.md)
  The user’s information.
- [CFURLComponentType.host](cfurlcomponenttype/host.md)
  The URL’s host.
- [CFURLComponentType.port](cfurlcomponenttype/port.md)
  The URL’s port.
- [CFURLComponentType.parameterString](cfurlcomponenttype/parameterstring.md)
  The URL’s parameter string.
- [CFURLComponentType.query](cfurlcomponenttype/query.md)
  The URL’s query.
- [CFURLComponentType.fragment](cfurlcomponenttype/fragment.md)
  The URL’s fragment.
### Initializers
- [init?(rawValue: CFIndex)](cfurlcomponenttype/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [enum CFURLPathStyle](cfurlpathstyle.md)
  Options you can use to determine how CFURL functions parse a file system path name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfurlcomponenttype)*