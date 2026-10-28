# kSecTransformAbortOriginatorKey

**Framework**: Security  
**Kind**: var  
**Role**: Global Variable

The key in an error’s `userInfo` dictionary whose value indicates the transform that caused the chain to abort.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
let kSecTransformAbortOriginatorKey: CFString
```

```c
extern CFStringRef const kSecTransformAbortOriginatorKey;
```

## Discussion

Use the value associated with this key to determine exactly which transform failed when more than one error occurs during transform evaluation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/ksectransformabortoriginatorkey)*