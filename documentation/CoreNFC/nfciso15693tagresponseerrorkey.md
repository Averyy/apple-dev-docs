# NFCISO15693TagResponseErrorKey

**Framework**: Core NFC  
**Kind**: var

A user information dictionary key indicating that a tag responded with a command error.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+

## Declaration

```swift
let NFCISO15693TagResponseErrorKey: String
```

#### Discussion

Check for the presence of this key in the [`userInfo`](https://developer.apple.com/documentation/foundation/nserror/1411580-userinfo) dictionary of an [`NSError`](https://developer.apple.com/documentation/Foundation/NSError) object to determine whether a tag responded with a command error. When a command error occurs, the [`code`](https://developer.apple.com/documentation/foundation/nserror/1409165-code) property contains an error code defined in the ISO15693-3 specification.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/nfciso15693tagresponseerrorkey)*