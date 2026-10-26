# content

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The content to append to the note.

**Availability**:
- iOS 11.0+ - Deprecated in 15.0
- iPadOS 11.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 4.0+ - Deprecated in 8.0

> **Deprecated**: This intent is no longer available. You may define a custom intent instead. For more information, see [Deprecated SiriKit Intent Domains](https://developer.apple.com/support/deprecated-sirikit-intent-domains).

## Declaration

```swift
@NSCopying
var content: INNoteContent? { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readonly, nullable) INNoteContent * content;
```

*macOS*

```objc
@property (atomic, copy, readonly, nullable) INNoteContent * content;
```

## See Also

### Getting the Note Content
- [var targetNote: INNote?](./targetnote.md)
  The note to receive the additional content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inappendtonoteintent/content)*