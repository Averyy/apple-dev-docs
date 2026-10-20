# NSApplication.OcclusionState

**Framework**: AppKit  
**Kind**: struct  
**Role**: Structure

This constant indicates whether at least part of any window owned by this app is visible.

**Availability**:
- macOS 10.9+

## Declaration

```swift
struct OcclusionState
```

```c
enum NSApplicationOcclusionState : NSUInteger;
```

## Topics

### Constants
- [static var visible: NSApplication.OcclusionState](./occlusionstate-swift.struct/visible.md)
  If set, at least part of any window owned by this app is visible.
### Initializers
- [init(rawValue: UInt)](./occlusionstate-swift.struct/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../../Swift/optionset.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)
- [SetAlgebra](../../Swift/setalgebra.md)

## See Also

### Getting the Occlusion State
- [var occlusionState: NSApplication.OcclusionState](./occlusionstate-swift.property.md)
  The occlusion state of the app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplication/occlusionstate-swift.struct)*