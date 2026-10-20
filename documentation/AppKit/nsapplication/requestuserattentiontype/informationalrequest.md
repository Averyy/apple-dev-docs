# NSApplication.RequestUserAttentionType.informationalRequest

**Framework**: AppKit  
**Kind**: case  
**Role**: Case

The user attention request is an informational request.

**Availability**:
- macOS

## Declaration

```swift
case informationalRequest
```

```c
NSInformationalRequest
```

#### Discussion

The dock icon will bounce for one second. The request, though, remains active until either the app becomes active or the request is canceled.

## See Also

### Constants
- [NSApplication.RequestUserAttentionType.criticalRequest](./criticalrequest.md)
  The user attention request is a critical request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplication/requestuserattentiontype/informationalrequest)*