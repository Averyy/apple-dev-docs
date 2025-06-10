# CFURLError

**Framework**: Core Foundation  
**Kind**: enum

`CFURL` error codes.

**Availability**:
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
enum CFURLError
```

## Topics

### Constants
- [CFURLError.unknownError](cfurlerror/unknownerror.md)
  Indicates an unknown error.
- [CFURLError.unknownSchemeError](cfurlerror/unknownschemeerror.md)
  Indicates that the scheme is not recognized.
- [CFURLError.resourceNotFoundError](cfurlerror/resourcenotfounderror.md)
  Indicates a resource was not found.
- [CFURLError.resourceAccessViolationError](cfurlerror/resourceaccessviolationerror.md)
  Indicates an error in accessing a resource.
- [CFURLError.remoteHostUnavailableError](cfurlerror/remotehostunavailableerror.md)
  Indicates a remote host is unavailable.
- [CFURLError.improperArgumentsError](cfurlerror/improperargumentserror.md)
  Indicates one or more arguments are improper.
- [CFURLError.unknownPropertyKeyError](cfurlerror/unknownpropertykeyerror.md)
  Indicates a property key is unknown.
- [CFURLError.propertyKeyUnavailableError](cfurlerror/propertykeyunavailableerror.md)
  Indicates a property key was unavailable.
- [CFURLError.timeoutError](cfurlerror/timeouterror.md)
  Indicates a timeout.
### Initializers
- [init?(rawValue: CFIndex)](cfurlerror/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [File URL Properties](file-url-properties.md)
  Properties for file URL resources.
- [HTTP URL Properties](http-url-properties.md)
  Properties for HTTP URL resources.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfurlerror)*