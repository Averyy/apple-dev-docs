# NSMediaLibraryBrowserController.Library

**Framework**: AppKit  
**Kind**: struct  
**Role**: Structure

These constants are masks used to configure a Media Library Browser to display specific types of media. Combined masks are not yet supported.  In other words, only one nonzero mask value is supported at a time.  If masks are combined, the lowest mask value is used.

**Availability**:
- macOS 10.9+

## Declaration

```swift
struct Library
```

```c
enum NSMediaLibrary : NSUInteger;
```

## Topics

### Constants
- [static var audio: NSMediaLibraryBrowserController.Library](./library/audio.md)
  Display audio media.
- [static var image: NSMediaLibraryBrowserController.Library](./library/image.md)
  Display image media.
- [static var movie: NSMediaLibraryBrowserController.Library](./library/movie.md)
  Display movie media.
### Initializers
- [init(rawValue: UInt)](./library/init%28rawvalue%29.md)

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmedialibrarybrowsercontroller/library)*