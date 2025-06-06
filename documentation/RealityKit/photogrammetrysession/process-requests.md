# process(requests:)

**Framework**: Realitykit  
**Kind**: method

Starts processing of the provided processing `requests`.  Messages begin to be produced to the `output` publisher.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 15.0+
- macOS 12.0+

## Declaration

```swift
func process(requests: [PhotogrammetrySession.Request]) throws
```

## Mentions

- [Creating 3D objects from photographs](creating-3d-objects-from-photographs.md)

#### Discussion

On the first `process()`call the data in the input source will be ingested entirely and `inputComplete` produced on the `output` stream before any request processing progress will begin. Before `inputComplete`, warnings about samples will be published, if any.

> **Note**: If `isProcessing` another batch still, the session is invalid (an Error was produced on `output` or if one of the requests is invalid.

## See Also

- [func cancel()](photogrammetrysession/cancel.md)
  Requests cancellation of any running requests.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/photogrammetrysession/process(requests:))*