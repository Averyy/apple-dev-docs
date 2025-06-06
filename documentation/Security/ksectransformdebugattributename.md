# kSecTransformDebugAttributeName

**Framework**: Security  
**Kind**: var

A write stream that should receive debug data.

**Availability**:
- macOS 10.7+

## Declaration

```swift
let kSecTransformDebugAttributeName: CFString
```

#### Discussion

Set this attribute to a [`CFWriteStream`](https://developer.apple.com/documentation/CoreFoundation/CFWriteStream). This signals the transform to write debugging information to the stream. If you set this attribute to [`kCFBooleanTrue`](https://developer.apple.com/documentation/CoreFoundation/kCFBooleanTrue), debug data is written to `stderr` instead.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/ksectransformdebugattributename)*