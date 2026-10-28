# CFURLComponentType

**Framework**: Core Foundation  
**Kind**: enum  
**Role**: Enumeration

The types of components in a URL.

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
enum CFURLComponentType
```

```c
enum CFURLComponentType : CFIndex;
```

## Overview

These constants are used by the [`CFURLGetByteRangeForComponent(_:_:_:)`](./cfurlgetbyterangeforcomponent%28_,_,_%29.md) function.

## Topics

### Constants
- [CFURLComponentType.scheme](./cfurlcomponenttype/scheme.md)
  The URL’s scheme.
- [CFURLComponentType.netLocation](./cfurlcomponenttype/netlocation.md)
  The URL’s network location.
- [CFURLComponentType.path](./cfurlcomponenttype/path.md)
  The URL’s path component.
- [CFURLComponentType.resourceSpecifier](./cfurlcomponenttype/resourcespecifier.md)
  The URL’s resource specifier.
- [CFURLComponentType.user](./cfurlcomponenttype/user.md)
  The URL’s user.
- [CFURLComponentType.password](./cfurlcomponenttype/password.md)
  The user’s password.
- [CFURLComponentType.userInfo](./cfurlcomponenttype/userinfo.md)
  The user’s information.
- [CFURLComponentType.host](./cfurlcomponenttype/host.md)
  The URL’s host.
- [CFURLComponentType.port](./cfurlcomponenttype/port.md)
  The URL’s port.
- [CFURLComponentType.parameterString](./cfurlcomponenttype/parameterstring.md)
  The URL’s parameter string.
- [CFURLComponentType.query](./cfurlcomponenttype/query.md)
  The URL’s query.
- [CFURLComponentType.fragment](./cfurlcomponenttype/fragment.md)
  The URL’s fragment.
### Initializers
- [init?(rawValue: CFIndex)](./cfurlcomponenttype/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Miscellaneous
- [enum CFURLPathStyle](./cfurlpathstyle.md)
  Options you can use to determine how CFURL functions parse a file system path name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfurlcomponenttype)*