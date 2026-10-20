# MCError.Code.timedOut

**Framework**: Multipeer Connectivity  
**Kind**: case  
**Role**: Case

The connection attempt timed out.

**Availability**:
- iOS 7.0+ - Deprecated in 27.0
- iPadOS 7.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- macOS 10.10+ - Deprecated in 27.0
- tvOS 10.0+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0

> **Deprecated**: Use Network Framework instead

## Declaration

```swift
case timedOut
```

```c
MCErrorTimedOut
```

## See Also

### Constants
- [MCError.Code.unknown](./unknown.md)
  An unknown error occurred.
- [MCError.Code.notConnected](./notconnected.md)
  Your app attempted to send data to a peer that is not connected.
- [MCError.Code.invalidParameter](./invalidparameter.md)
  Your app passed an invalid value as a parameter.
- [MCError.Code.unsupported](./unsupported.md)
  The operation is unsupported. For example, this error is returned if you call [`sendResource(at:withName:toPeer:withCompletionHandler:)`](../../mcsession/sendresource%28at,withname,topeer,withcompletionhandler%29.md) with a URL that is neither a local file nor a web URL.
- [MCError.Code.cancelled](./cancelled.md)
  The operation was cancelled by the user.
- [MCError.Code.unavailable](./unavailable.md)
  Multipeer connectivity is currently unavailable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/multipeerconnectivity/mcerror/code/timedout)*