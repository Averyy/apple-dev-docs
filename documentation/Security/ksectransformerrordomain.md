# kSecTransformErrorDomain

**Framework**: Security  
**Kind**: var  
**Role**: Global Variable

The domain of any error object created by a transform on failure.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
let kSecTransformErrorDomain: CFString
```

```c
extern CFStringRef const kSecTransformErrorDomain;
```

#### Discussion

Use this [`CFError`](../CoreFoundation/cferror.md) object to determine what went wrong.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/ksectransformerrordomain)*