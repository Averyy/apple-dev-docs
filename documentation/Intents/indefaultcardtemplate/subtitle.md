# subtitle

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The subtitle displayed in the Siri watch face card.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
var subtitle: String? { get set }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, nullable) NSString * subtitle;
```

*macOS*

```objc
@property (atomic, copy, nullable) NSString * subtitle;
```

## Mentions

- [Displaying Shortcut Information in a Siri Watch Face Card](../../SiriKit/displaying-shortcut-information-in-a-siri-watch-face-card.md)

## Discussion

If you don’t provide a [`subtitle`](./subtitle.md), the text from [`title`](./title.md) will wrap to fill two lines.

## See Also

### Managing Template Information
- [var title: String](./title.md)
  The title displayed in the Siri watch face card.
- [var image: INImage?](./image.md)
  The image displayed in the Siri watch face card.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/indefaultcardtemplate/subtitle)*