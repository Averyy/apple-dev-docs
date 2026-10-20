# CFURLError

**Framework**: Core Foundation  
**Kind**: enum  
**Role**: Enumeration

`CFURL` error codes.

**Availability**:
- iOS 2.0+ - Deprecated in 7.0
- iPadOS 2.0+ - Deprecated in 7.0
- Mac Catalyst 2.0+ - Deprecated in 7.0
- tvOS 9.0+ - Deprecated in 9.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 2.0+ - Deprecated in 2.0

> **Deprecated**: Use CFError codes instead

## Declaration

```swift
enum CFURLError
```

```c
enum CFURLError : CFIndex;
```

## Topics

### Constants
- [CFURLError.unknownError](./cfurlerror/unknownerror.md)
  Indicates an unknown error.
- [CFURLError.unknownSchemeError](./cfurlerror/unknownschemeerror.md)
  Indicates that the scheme is not recognized.
- [CFURLError.resourceNotFoundError](./cfurlerror/resourcenotfounderror.md)
  Indicates a resource was not found.
- [CFURLError.resourceAccessViolationError](./cfurlerror/resourceaccessviolationerror.md)
  Indicates an error in accessing a resource.
- [CFURLError.remoteHostUnavailableError](./cfurlerror/remotehostunavailableerror.md)
  Indicates a remote host is unavailable.
- [CFURLError.improperArgumentsError](./cfurlerror/improperargumentserror.md)
  Indicates one or more arguments are improper.
- [CFURLError.unknownPropertyKeyError](./cfurlerror/unknownpropertykeyerror.md)
  Indicates a property key is unknown.
- [CFURLError.propertyKeyUnavailableError](./cfurlerror/propertykeyunavailableerror.md)
  Indicates a property key was unavailable.
- [CFURLError.timeoutError](./cfurlerror/timeouterror.md)
  Indicates a timeout.
### Initializers
- [init?(rawValue: CFIndex)](./cfurlerror/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Constants
- [File URL Properties](./file-url-properties.md)
  Properties for file URL resources.
- [HTTP URL Properties](./http-url-properties.md)
  Properties for HTTP URL resources.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfurlerror)*