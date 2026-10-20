# SSLContext

**Framework**: Security  
**Kind**: class  
**Role**: Class

An opaque type that represents an SSL session context object.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
class SSLContext
```

```c
typedef struct SSLContext * SSLContextRef;
```

#### Overview

The SSL session context object references the state associated with a session. You can’t reuse an SSL session context in multiple sessions.

## Relationships

### Conforms To
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sslcontext)*