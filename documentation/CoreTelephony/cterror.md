# CTError

**Framework**: Core Telephony  
**Kind**: struct

A type representing a Core Telephony error.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 14.0+
- macOS 10.10+

## Declaration

```swift
struct CTError
```

## Topics

### Getting Error Properties
- [var domain: Int32](cterror/domain.md)
  A numeric indication of the error domain.
- [var error: Int32](cterror/error.md)
  A code indicating the specific error.
### Identifying Error Domains
- [Error Domains](error-domain-codes.md)
  Error domains used by Core Telephony errors.
### Initializers
- [init()](cterror/init.md)
  Creates a Core Telephony error instance.
- [init(domain: Int32, error: Int32)](cterror/init(domain:error:).md)
  Creates a Core Telephony error instance with the given values.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Sendable](../Swift/Sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretelephony/cterror)*