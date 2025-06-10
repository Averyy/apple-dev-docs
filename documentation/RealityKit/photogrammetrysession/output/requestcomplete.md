# PhotogrammetrySession.Output.requestComplete(_:_:)

**Framework**: RealityKit  
**Kind**: case

The session finished handling all pending requests.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 15.0+
- macOS 12.0+

## Declaration

```swift
case requestComplete(PhotogrammetrySession.Request, PhotogrammetrySession.Result)
```

## See Also

- [case requestProgress(PhotogrammetrySession.Request, fractionComplete: Double)](photogrammetrysession/output/requestprogress(_:fractioncomplete:).md)
  A progress update provided by the session.
- [case requestError(PhotogrammetrySession.Request, any Error)](photogrammetrysession/output/requesterror(_:_:).md)
  The session aborted a request due to an error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/photogrammetrysession/output/requestcomplete(_:_:))*