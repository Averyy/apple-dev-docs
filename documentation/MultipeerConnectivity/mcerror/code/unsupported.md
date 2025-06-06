# MCError.Code.unsupported

**Framework**: Multipeer Connectivity  
**Kind**: case

The operation is unsupported. For example, this error is returned if you call [`sendResource(at:withName:toPeer:withCompletionHandler:)`](mcsession/sendresource(at:withname:topeer:withcompletionhandler:).md) with a URL that is neither a local file nor a web URL.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
case unsupported
```

## See Also

- [MCError.Code.unknown](mcerror/code/unknown.md)
  An unknown error occurred.
- [MCError.Code.notConnected](mcerror/code/notconnected.md)
  Your app attempted to send data to a peer that is not connected.
- [MCError.Code.invalidParameter](mcerror/code/invalidparameter.md)
  Your app passed an invalid value as a parameter.
- [MCError.Code.timedOut](mcerror/code/timedout.md)
  The connection attempt timed out.
- [MCError.Code.cancelled](mcerror/code/cancelled.md)
  The operation was cancelled by the user.
- [MCError.Code.unavailable](mcerror/code/unavailable.md)
  Multipeer connectivity is currently unavailable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/multipeerconnectivity/mcerror/code/unsupported)*