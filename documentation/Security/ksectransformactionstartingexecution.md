# kSecTransformActionStartingExecution

**Framework**: Security  
**Kind**: var  
**Role**: Global Variable

An action that triggers just before starting execution of a custom transform.

**Availability**:
- macOS 10.7+ - Deprecated in 13.0

> **Deprecated**: SecTransform is no longer supported

## Declaration

```swift
let kSecTransformActionStartingExecution: CFString
```

```c
extern CFStringRef const kSecTransformActionStartingExecution;
```

#### Discussion

Overrides the standard behavior that occurs just before starting execution of a custom transform. This is typically overridden to allow for initialization. This is used with the SecTransformOverrideTransformAction block.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/ksectransformactionstartingexecution)*