# SecCodeValidateFileResource(_:_:_:_:)

**Framework**: Security  
**Kind**: func  
**Role**: Function

**Availability**:
- macOS 10.13+

## Declaration

```swift
func SecCodeValidateFileResource(_ code: SecStaticCode, _ relativePath: CFString, _ fileData: CFData, _ flags: SecCSFlags) -> OSStatus
```

```c
OSStatus SecCodeValidateFileResource(SecStaticCodeRef code, CFStringRef relativePath, CFDataRef fileData, SecCSFlags flags);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/seccodevalidatefileresource(_:_:_:_:))*