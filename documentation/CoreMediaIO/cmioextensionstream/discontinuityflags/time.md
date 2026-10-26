# time

**Framework**: Core Media I/O  
**Kind**: property  
**Role**: Type Property

A flag that indicates a time discontinuity in the stream.

**Availability**:
- Mac Catalyst 15.4+
- macOS 12.3+

## Declaration

```swift
static var time: CMIOExtensionStream.DiscontinuityFlags { get }
```

```c
CMIOExtensionStreamDiscontinuityFlagTime
```

## See Also

### Discontinuity Flags
- [static var unknown: CMIOExtensionStream.DiscontinuityFlags](./unknown.md)
  A flag that indicates a stream discontinuity due to an unknown reason.
- [static var sampleDropped: CMIOExtensionStream.DiscontinuityFlags](./sampledropped.md)
  A flag that indicates a discontinuity in the stream due to a dropped frame.
- [CMIOExtensionStreamDiscontinuityFlagNone](../../cmioextensionstreamdiscontinuityflags/cmioextensionstreamdiscontinuityflagnone.md)
  A flag that indicates there’s no discontinuity in the stream.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremediaio/cmioextensionstream/discontinuityflags/time)*