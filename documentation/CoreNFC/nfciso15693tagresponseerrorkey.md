# NFCISO15693TagResponseErrorKey

**Framework**: Core NFC  
**Kind**: var  
**Role**: Global Variable

A user information dictionary key indicating that a tag responded with a command error.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+

## Declaration

```swift
let NFCISO15693TagResponseErrorKey: String
```

```c
extern NSString * const NFCISO15693TagResponseErrorKey;
```

## Discussion

Check for the presence of this key in the [`userInfo`](../Foundation/nserror/userinfo.md) dictionary of an [`NSError`](../Foundation/nserror.md) object to determine whether a tag responded with a command error. When a command error occurs, the [`code`](../Foundation/nserror/code.md) property contains an error code defined in the ISO15693-3 specification.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/nfciso15693tagresponseerrorkey)*