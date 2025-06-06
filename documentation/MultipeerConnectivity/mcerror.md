# MCError

**Framework**: Multipeer Connectivity  
**Kind**: struct

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
struct MCError
```

## Topics

### Initializers
- [init(Code, userInfo: [String : Any])](mcerror/3726664-init.md)
### Instance Properties
- [var code: Code](mcerror/3726661-code.md)
- [var errorCode: Int](mcerror/2887194-errorcode.md)
- [var errorUserInfo: [String : Any]](mcerror/2887196-erroruserinfo.md)
- [var hashValue: Int](mcerror/3726663-hashvalue.md)
- [var userInfo: [String : Any]](mcerror/3726665-userinfo.md)
### Type Properties
- [static var cancelled: MCError.Code](mcerror/cancelled.md)
- [static var errorDomain: String](mcerror/errordomain.md)
- [static var invalidParameter: MCError.Code](mcerror/invalidparameter.md)
- [static var notConnected: MCError.Code](mcerror/notconnected.md)
- [static var timedOut: MCError.Code](mcerror/timedout.md)
- [static var unavailable: MCError.Code](mcerror/unavailable.md)
- [static var unknown: MCError.Code](mcerror/unknown.md)
- [static var unsupported: MCError.Code](mcerror/unsupported.md)
### Instance Methods
- [func hash(into: inout Hasher)](mcerror/3726662-hash.md)
### Operator Functions
- [static func == (MCError, MCError) -> Bool](mcerror/3726660.md)
### Enumerations
- [MCError.Code](mcerror/code.md)
  Error codes found in [`MCErrorDomain`](mcerrordomain.md) error domain `NSError` objects returned by methods in the Multipeer Connectivity framework.

## Relationships

### Conforms To
- [CustomNSError](../Foundation/CustomNSError.md)
- [Equatable](../Swift/Equatable.md)
- [Error](../Swift/Error.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/multipeerconnectivity/mcerror)*