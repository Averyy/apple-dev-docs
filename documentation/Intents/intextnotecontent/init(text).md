# init(text:)

**Framework**: Intents  
**Kind**: init  
**Role**: Initializer

Initializes a text-based note with the specified content.

**Availability**:
- iOS 11.0+ - Deprecated in 27.0
- iPadOS 11.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0
- watchOS 4.0+ - Deprecated in 27.0

> **Deprecated**: INTextNoteContent is deprecated. Please adopt the Notes or Reminders AppSchema domain instead.

## Declaration

```swift
init(text: String)
```

```objc
- (instancetype) initWithText:(NSString *) text;
```

#### Return Value

An initialized text note object or `nil` if the object could not be created.

## Parameters

- `text`: The text to include in the main content of the note.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/intextnotecontent/init(text:))*