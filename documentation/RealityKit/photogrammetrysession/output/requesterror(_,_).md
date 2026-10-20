# PhotogrammetrySession.Output.requestError(_:_:)

**Framework**: RealityKit  
**Kind**: case  
**Role**: Case

The session aborted a request due to an error.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 15.0+
- macOS 12.0+

## Declaration

```swift
case requestError(PhotogrammetrySession.Request, any Error)
```

## Parameters

- `Request`: The request in progress.
- `Error`: Details of the error.

## See Also

### Monitoring request status
- [case requestProgress(PhotogrammetrySession.Request, fractionComplete: Double)](./requestprogress%28_,fractioncomplete%29.md)
  A progress update provided by the session.
- [case requestComplete(PhotogrammetrySession.Request, PhotogrammetrySession.Result)](./requestcomplete%28_,_%29.md)
  The session finished handling all pending requests.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/photogrammetrysession/output/requesterror(_:_:))*