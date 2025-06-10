# PhotogrammetrySession.Output.requestProgress(_:fractionComplete:)

**Framework**: RealityKit  
**Kind**: case

A progress update provided by the session.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 15.0+
- macOS 12.0+

## Declaration

```swift
case requestProgress(PhotogrammetrySession.Request, fractionComplete: Double)
```

## Parameters

- `Request`: The request in progress.
- `fractionComplete`: A number from   to   indicating the current progress for the request.

## See Also

- [case requestComplete(PhotogrammetrySession.Request, PhotogrammetrySession.Result)](photogrammetrysession/output/requestcomplete(_:_:).md)
  The session finished handling all pending requests.
- [case requestError(PhotogrammetrySession.Request, any Error)](photogrammetrysession/output/requesterror(_:_:).md)
  The session aborted a request due to an error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/photogrammetrysession/output/requestprogress(_:fractioncomplete:))*