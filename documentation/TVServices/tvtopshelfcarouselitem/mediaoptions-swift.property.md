# mediaOptions

**Framework**: TV Services  
**Kind**: property  
**Role**: Instance Property

Information about the media format and presentation options.

**Availability**:
- tvOS 13.0+

## Declaration

```swift
var mediaOptions: TVTopShelfCarouselItem.MediaOptions { get set }
```

```objc
@property (nonatomic) TVTopShelfCarouselItemMediaOptions mediaOptions;
```

#### Discussion

Specify all of the options that apply to the underlying content. The system adds standard icons for the options you support. For example, if you specify the [`videoResolution4K`](./mediaoptions-swift.struct/videoresolution4k.md) option, the system adds an icon to the detail view indicating that playback in 4K resolution is possible.

## See Also

### Adding Media Badges
- [TVTopShelfCarouselItem.MediaOptions](./mediaoptions-swift.struct.md)
  Constants indicating the item’s audio and video capabilities.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvservices/tvtopshelfcarouselitem/mediaoptions-swift.property)*