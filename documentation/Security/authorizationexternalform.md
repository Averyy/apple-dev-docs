# AuthorizationExternalForm

**Framework**: Security  
**Kind**: struct

The external representation of an authorization reference.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
struct AuthorizationExternalForm
```

#### Overview

Authorization references are bound by session, process, and time limits, so you can’t store the authorization references for another process to use. Use the functions [`AuthorizationMakeExternalForm(_:_:)`](authorizationmakeexternalform(_:_:).md) and [`AuthorizationCreateFromExternalForm(_:_:)`](authorizationcreatefromexternalform(_:_:).md) to externalize and internalize the authorization reference. Apps should take care not to disclose the external authorization reference to potential attackers since any process can use this external authorization reference to access the authorization reference.

## Topics

### Initializers
- [init()](authorizationexternalform/init.md)
- [init(bytes: (CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar))](authorizationexternalform/init(bytes:).md)
### Instance Properties
- [var bytes: (CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar, CChar)](authorizationexternalform/bytes.md)
  An array of characters representing the external form of an authorization reference.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Sendable](../Swift/Sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/authorizationexternalform)*