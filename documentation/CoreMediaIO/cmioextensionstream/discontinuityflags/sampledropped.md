# sampleDropped

**Framework**: Core Media I/O  
**Kind**: property  
**Role**: Type Property

A flag that indicates a discontinuity in the stream due to a dropped frame.

**Availability**:
- Mac Catalyst 15.4+
- macOS 12.3+

## Declaration

```swift
static var sampleDropped: CMIOExtensionStream.DiscontinuityFlags { get }
```

```c
CMIOExtensionStreamDiscontinuityFlagSampleDropped
```

## See Also

### Discontinuity Flags
- [static var unknown: CMIOExtensionStream.DiscontinuityFlags](./unknown.md)
  A flag that indicates a stream discontinuity due to an unknown reason.
- [static var time: CMIOExtensionStream.DiscontinuityFlags](./time.md)
  A flag that indicates a time discontinuity in the stream.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremediaio/cmioextensionstream/discontinuityflags/sampledropped)*