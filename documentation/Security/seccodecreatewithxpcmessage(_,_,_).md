# SecCodeCreateWithXPCMessage(_:_:_:)

**Framework**: Security  
**Kind**: func  
**Role**: Function

**Availability**:
- macOS 10.0+

## Declaration

```swift
func SecCodeCreateWithXPCMessage(_ message: xpc_object_t, _ flags: SecCSFlags, _ target: UnsafeMutablePointer<SecCode?>) -> OSStatus
```

```c
OSStatus SecCodeCreateWithXPCMessage(xpc_object_t message, SecCSFlags flags, SecCodeRef*target);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/seccodecreatewithxpcmessage(_:_:_:))*