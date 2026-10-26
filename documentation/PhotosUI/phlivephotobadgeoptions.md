# PHLivePhotoBadgeOptions

**Framework**: PhotosUI  
**Kind**: struct  
**Role**: Structure

Options for the semantic use and display style of icons for badging Live Photo assets, used by the [`livePhotoBadgeImage(options:)`](./phlivephotoview/livephotobadgeimage%28options%29.md) method.

**Availability**:
- iOS 9.1+
- iPadOS 9.1+
- Mac Catalyst 13.1+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
struct PHLivePhotoBadgeOptions
```

```c
enum PHLivePhotoBadgeOptions : NSUInteger;
```

## Topics

### Initializers
- [init(rawValue: UInt)](./phlivephotobadgeoptions/init%28rawvalue%29.md)
  Creates Live Photo badge options from a raw value.
### Constants
- [static var liveOff: PHLivePhotoBadgeOptions](./phlivephotobadgeoptions/liveoff.md)
  Return an icon for identifying assets whose additional Live Photo content is disabled.
- [static var overContent: PHLivePhotoBadgeOptions](./phlivephotobadgeoptions/overcontent.md)
  Return a variant icon for use on a variable background such as an animating Live Photo view.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../Swift/optionset.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [SetAlgebra](../Swift/setalgebra.md)

## See Also

### Constants
- [enum PHLivePhotoViewPlaybackStyle](./phlivephotoviewplaybackstyle.md)
  Options for how much of the motion and sound content of a Live Photo to play, used in the [`startPlayback(with:)`](./phlivephotoview/startplayback%28with%29.md) method and in messages to the view’s [`delegate`](./phlivephotoview/delegate.md) object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photosui/phlivephotobadgeoptions)*