# PhotogrammetrySession.Request.Detail.raw

**Framework**: RealityKit  
**Kind**: case

The raw-created object at the highest possible resolution.

**Availability**:
- Mac Catalyst 15.0+
- macOS 12.0+

## Declaration

```swift
case raw
```

#### Discussion

Use this option only for creating high-end production assets.. This will generate unprocessed assets that allow professional artists using physically-based rendering ray-tracers to achieve maximum quality results. The output of a raw request is unsuitable for real-time use.

## See Also

- [PhotogrammetrySession.Request.Detail.preview](photogrammetrysession/request/detail/preview.md)
  A fast, low-quality object for previewing the final result.
- [PhotogrammetrySession.Request.Detail.reduced](photogrammetrysession/request/detail/reduced.md)
  A mobile-quality object with low resource requirements.
- [PhotogrammetrySession.Request.Detail.medium](photogrammetrysession/request/detail/medium.md)
  A medium-quality object with moderate resource requirements.
- [PhotogrammetrySession.Request.Detail.full](photogrammetrysession/request/detail/full.md)
  A high-quality object with significant resource requirements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/photogrammetrysession/request/detail/raw)*