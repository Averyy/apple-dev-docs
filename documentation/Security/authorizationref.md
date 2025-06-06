# AuthorizationRef

**Framework**: Security  
**Kind**: typealias

A pointer to an opaque authorization reference structure.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
typealias AuthorizationRef = OpaquePointer
```

#### Discussion

This data type points to a structure the Security Server uses to store information about the authorization session. Use the functions described in [`Authorization Services`](authorization-services.md) to create, access, and free the authorization reference.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/authorizationref)*