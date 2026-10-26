# groupName

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The group that contains the note.

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
var groupName: INSpeakableString? { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readonly, nullable) INSpeakableString * groupName;
```

*macOS*

```objc
@property (atomic, copy, readonly, nullable) INSpeakableString * groupName;
```

#### Discussion

Use groups to organize notes within your app. For example, a group might correspond to a folder that contains related notes. The group name should correspond to the user-visible name of the group in your app.

## See Also

### Getting the Note Content
- [var title: INSpeakableString?](./title.md)
  The title text for the note.
- [var content: INNoteContent?](./content.md)
  The main content of the note.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/increatenoteintent/groupname)*