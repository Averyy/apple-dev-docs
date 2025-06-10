# PhotogrammetrySession.Output.inputComplete

**Framework**: RealityKit  
**Kind**: case

The data ingestion portion of the process is complete.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 15.0+
- macOS 12.0+

## Declaration

```swift
case inputComplete
```

#### Discussion

Once the session sends this messagae, processing on the actual requests begins. It only sends this on the first `process()` call after which the data from the original processing is reused.

## See Also

- [PhotogrammetrySession.Output.processingComplete](photogrammetrysession/output/processingcomplete.md)
  The session completed a request successfully.
- [PhotogrammetrySession.Output.processingCancelled](photogrammetrysession/output/processingcancelled.md)
  All pending requests are canceled.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/photogrammetrysession/output/inputcomplete)*