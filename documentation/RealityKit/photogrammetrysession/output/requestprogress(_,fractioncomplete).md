# PhotogrammetrySession.Output.requestProgress(_:fractionComplete:)

**Framework**: RealityKit  
**Kind**: case  
**Role**: Case

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
- `fractionComplete`: A number from `0.0` to `1.0` indicating the current progress for the request.

## See Also

### Monitoring request status
- [case requestComplete(PhotogrammetrySession.Request, PhotogrammetrySession.Result)](./requestcomplete%28_,_%29.md)
  The session finished handling all pending requests.
- [case requestError(PhotogrammetrySession.Request, any Error)](./requesterror%28_,_%29.md)
  The session aborted a request due to an error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/photogrammetrysession/output/requestprogress(_:fractioncomplete:))*