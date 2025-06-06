# CFSocketCallBack

**Framework**: Core Foundation  
**Kind**: typealias

Callback invoked when certain types of activity takes place on a CFSocket object.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
typealias CFSocketCallBack = (CFSocket?, CFSocketCallBackType, CFData?, UnsafeRawPointer?, UnsafeMutableRawPointer?) -> Void
```

#### Discussion

You specify this callback when you create the CFSocket object with [`CFSocketCreate(_:_:_:_:_:_:_:)`](cfsocketcreate(_:_:_:_:_:_:_:).md), [`CFSocketCreateConnectedToSocketSignature(_:_:_:_:_:_:)`](cfsocketcreateconnectedtosocketsignature(_:_:_:_:_:_:).md), [`CFSocketCreateWithNative(_:_:_:_:_:)`](cfsocketcreatewithnative(_:_:_:_:_:).md), or [`CFSocketCreateWithSocketSignature(_:_:_:_:_:)`](cfsocketcreatewithsocketsignature(_:_:_:_:_:).md).

## Parameters

- `s`: The CFSocket object that experienced some activity.
- `callbackType`: The type of activity detected.
- `address`: A CFData object holding the contents of a   appropriate for the protocol family of   (  or  , for example), identifying the remote address to which   is connected. This value is   except for   and   callbacks.
- `data`: Data appropriate for the callback type. For a   that failed in the background, it is a pointer to an   error code; for a  , it is a pointer to a  ; or for a  , it is a CFData object containing the incoming data. In all other cases, it is  .
- `info`: The   member of the   structure that was used when creating the CFSocket object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfsocketcallback)*