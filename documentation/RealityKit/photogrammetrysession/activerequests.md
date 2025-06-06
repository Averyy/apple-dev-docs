# activeRequests

**Framework**: RealityKit  
**Kind**: property

The session’s active request objects.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 15.0+
- macOS 12.0+

## Declaration

```swift
var activeRequests: [PhotogrammetrySession.Request] { get }
```

#### Discussion

This property provides read-only access to the requests that the session actively processes.

## See Also

- [var isProcessing: Bool](photogrammetrysession/isprocessing.md)
  The session is actively processing requests.
- [var outputs: PhotogrammetrySession.Outputs](photogrammetrysession/outputs-swift.property.md)
  Returns the outputs message stream which can be asynchronously iterated on.
- [PhotogrammetrySession.Output](photogrammetrysession/output.md)
  Status updates on the object-creation process.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/photogrammetrysession/activerequests)*