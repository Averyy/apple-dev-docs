# kSecTransformActionFinalize

**Framework**: Security  
**Kind**: var

An action that triggers just before deleting a custom transform to enable custom cleanup operations.

**Availability**:
- macOS 10.7+

## Declaration

```swift
let kSecTransformActionFinalize: CFString
```

#### Discussion

Overrides the standard behavior that occurs just before deleting a custom transform. This is typically overridden to allow for memory clean up of a custom transform. This is used with the SecTransformOverrideTransformAction block.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/ksectransformactionfinalize)*