# CXErrorCodeIncomingCallError.Code.filteredByDoNotDisturb

**Framework**: CallKit  
**Kind**: case  
**Role**: Case

The incoming call is filtered because Do Not Disturb is active and the incoming caller is not a VIP.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 10.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
case filteredByDoNotDisturb
```

```c
CXErrorCodeIncomingCallErrorFilteredByDoNotDisturb
```

## See Also

### Errors
- [CXErrorCodeIncomingCallError.Code.unknown](./unknown.md)
  An unknown error occurred.
- [CXErrorCodeIncomingCallError.Code.unentitled](./unentitled.md)
  The app isn’t entitled to receive incoming calls.
- [CXErrorCodeIncomingCallError.Code.callUUIDAlreadyExists](./calluuidalreadyexists.md)
  The incoming call UUID already exists.
- [CXErrorCodeIncomingCallError.Code.filteredByBlockList](./filteredbyblocklist.md)
  The incoming call is filtered because the incoming caller has been blocked by the user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/callkit/cxerrorcodeincomingcallerror-swift.struct/code/filteredbydonotdisturb)*