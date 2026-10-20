# kSecTransformDebugAttributeName

**Framework**: Security  
**Kind**: var  
**Role**: Global Variable

A write stream that should receive debug data.

**Availability**:
- macOS 10.7+ - Deprecated in 12.0

> **Deprecated**: SecTransform is no longer supported

## Declaration

```swift
let kSecTransformDebugAttributeName: CFString
```

```c
extern CFStringRef const kSecTransformDebugAttributeName;
```

#### Discussion

Set this attribute to a [`CFWriteStream`](../CoreFoundation/cfwritestream.md). This signals the transform to write debugging information to the stream. If you set this attribute to [`kCFBooleanTrue`](../CoreFoundation/kcfbooleantrue.md), debug data is written to `stderr` instead.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/ksectransformdebugattributename)*