# image

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The image displayed in the Siri watch face card.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
@NSCopying
var image: INImage? { get set }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, nullable) INImage * image;
```

*macOS*

```objc
@property (atomic, copy, nullable) INImage * image;
```

## Mentions

- [Displaying Shortcut Information in a Siri Watch Face Card](../../SiriKit/displaying-shortcut-information-in-a-siri-watch-face-card.md)

#### Discussion

The image should be a square image. [`INDefaultCardTemplate`](../indefaultcardtemplate.md) automatically scales the image to fit and rounds the image corners, and the card template supports image transparency.

## See Also

### Managing Template Information
- [var title: String](./title.md)
  The title displayed in the Siri watch face card.
- [var subtitle: String?](./subtitle.md)
  The subtitle displayed in the Siri watch face card.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/indefaultcardtemplate/image)*