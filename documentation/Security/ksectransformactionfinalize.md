# kSecTransformActionFinalize

**Framework**: Security  
**Kind**: var  
**Role**: Global Variable

An action that triggers just before deleting a custom transform to enable custom cleanup operations.

**Availability**:
- macOS 10.7+ - Deprecated in 13.0

> **Deprecated**: SecTransform is no longer supported

## Declaration

```swift
let kSecTransformActionFinalize: CFString
```

```c
extern CFStringRef const kSecTransformActionFinalize;
```

#### Discussion

Overrides the standard behavior that occurs just before deleting a custom transform. This is typically overridden to allow for memory clean up of a custom transform. This is used with the SecTransformOverrideTransformAction block.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/ksectransformactionfinalize)*