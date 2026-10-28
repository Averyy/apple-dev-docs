# title

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The title text to search for in a note, task, or task list.

**Availability**:
- iOS 11.0+ - Deprecated in 27.0
- iPadOS 11.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0
- watchOS 4.0+ - Deprecated in 27.0

> **Deprecated**: INSearchForNotebookItemsIntent is deprecated. Please adopt the Notes or Reminders AppSchema domain instead.

## Declaration

```swift
@NSCopying
var title: INSpeakableString? { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readonly, nullable) INSpeakableString * title;
```

*macOS*

```objc
@property (atomic, copy, readonly, nullable) INSpeakableString * title;
```

## Discussion

When this property contains a valid string, search for that string in the title text of notes, tasks, or task lists. For notes, use this string to match only the portion of the note that you use to summarize the note to the user.

When the value of this property is `nil`, do not use the title text as part of your search criteria.

## See Also

### Searching by Content
- [var content: String?](./content.md)
  The text to search for in the body of a note.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insearchfornotebookitemsintent/title)*