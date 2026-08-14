# NSMediaLibraryBrowserController.Library

**Framework**: AppKit  
**Kind**: struct

These constants are masks used to configure a Media Library Browser to display specific types of media. Combined masks are not yet supported.  In other words, only one nonzero mask value is supported at a time.  If masks are combined, the lowest mask value is used.

**Availability**:
- macOS 10.9+

## Declaration

```swift
struct Library
```

## Topics

### Constants
- [static var audio: NSMediaLibraryBrowserController.Library](nsmedialibrarybrowsercontroller/library/audio.md)
  Display audio media.
- [static var image: NSMediaLibraryBrowserController.Library](nsmedialibrarybrowsercontroller/library/image.md)
  Display image media.
- [static var movie: NSMediaLibraryBrowserController.Library](nsmedialibrarybrowsercontroller/library/movie.md)
  Display movie media.
### Initializers
- [init(rawValue: UInt)](nsmedialibrarybrowsercontroller/library/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../swift/bitwisecopyable.md)
- [Equatable](../swift/equatable.md)
- [ExpressibleByArrayLiteral](../swift/expressiblebyarrayliteral.md)
- [OptionSet](../swift/optionset.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)
- [SetAlgebra](../swift/setalgebra.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmedialibrarybrowsercontroller/library)*