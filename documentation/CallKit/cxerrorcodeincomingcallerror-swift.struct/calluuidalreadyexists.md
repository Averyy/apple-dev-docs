# callUUIDAlreadyExists

**Framework**: CallKit  
**Kind**: property

The incoming call UUID already exists.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 10.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
static var callUUIDAlreadyExists: CXErrorCodeIncomingCallError.Code { get }
```

## See Also

- [static var filteredByBlockList: CXErrorCodeIncomingCallError.Code](cxerrorcodeincomingcallerror-swift.struct/filteredbyblocklist.md)
  The system is filtering the incoming call because the user is blocking it.
- [static var filteredByDoNotDisturb: CXErrorCodeIncomingCallError.Code](cxerrorcodeincomingcallerror-swift.struct/filteredbydonotdisturb.md)
  The system is filtering the incoming call because Do Not Disturb is active and the incoming caller isn’t a VIP.
- [static var unentitled: CXErrorCodeIncomingCallError.Code](cxerrorcodeincomingcallerror-swift.struct/unentitled.md)
  The app doesn’t have the entitlement to receive incoming calls.
- [static var unknown: CXErrorCodeIncomingCallError.Code](cxerrorcodeincomingcallerror-swift.struct/unknown.md)
  An unknown error occurred.


---

*[View on Apple Developer](https://developer.apple.com/documentation/callkit/cxerrorcodeincomingcallerror-swift.struct/calluuidalreadyexists)*