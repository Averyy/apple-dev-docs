# kSecTransformActionStartingExecution

**Framework**: Security  
**Kind**: var

An action that triggers just before starting execution of a custom transform.

**Availability**:
- macOS 10.7+

## Declaration

```swift
let kSecTransformActionStartingExecution: CFString
```

#### Discussion

Overrides the standard behavior that occurs just before starting execution of a custom transform. This is typically overridden to allow for initialization. This is used with the SecTransformOverrideTransformAction block.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/ksectransformactionstartingexecution)*