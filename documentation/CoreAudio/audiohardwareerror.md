# AudioHardwareError

**Framework**: Core Audio  
**Kind**: struct

Represents errors returned by the HAL

**Availability**:
- Mac Catalyst ?+
- macOS 15.0+

## Declaration

```swift
struct AudioHardwareError
```

## Topics

### Initializers
- [init(OSStatus)](audiohardwareerror/init(_:).md)
### Instance Properties
- [let error: OSStatus](audiohardwareerror/error.md)
- [var errorDescription: String?](audiohardwareerror/errordescription.md)
  Provides localized descriptions for the error constants unique to HAL . Note that the HAL’s functions can and will return other codes that are not covered here, in which case no description is provided.

## Relationships

### Conforms To
- [Error](../Swift/Error.md)
- [LocalizedError](../Foundation/LocalizedError.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreaudio/audiohardwareerror)*