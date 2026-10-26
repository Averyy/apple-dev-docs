# content

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The text to search for in the body of a note.

**Availability**:
- iOS 11.0+ - Deprecated in 27.0
- iPadOS 11.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0
- watchOS 4.0+ - Deprecated in 27.0

> **Deprecated**: INSearchForNotebookItemsIntent is deprecated. Please adopt the Notes or Reminders AppSchema domain instead.

## Declaration

```swift
var content: String? { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readonly, nullable) NSString * content;
```

*macOS*

```objc
@property (atomic, copy, readonly, nullable) NSString * content;
```

#### Discussion

When this property contains a valid string, search for that string in the body text of the user’s notes.

When the value of this property is `nil`, do not use the text as part of your search criteria.

## See Also

### Searching by Content
- [var title: INSpeakableString?](./title.md)
  The title text to search for in a note, task, or task list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insearchfornotebookitemsintent/content)*