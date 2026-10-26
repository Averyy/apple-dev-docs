# content

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The main content of the note.

**Availability**:
- iOS 11.0+ - Deprecated in 27.0
- iPadOS 11.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0
- watchOS 4.0+ - Deprecated in 27.0

> **Deprecated**: INCreateNoteIntent is deprecated. Please adopt the Notes or Reminders AppSchema domain instead.

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
- [var title: INSpeakableString?](./title.md)
  The title text for the note.
- [var groupName: INSpeakableString?](./groupname.md)
  The group that contains the note.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/increatenoteintent/content)*