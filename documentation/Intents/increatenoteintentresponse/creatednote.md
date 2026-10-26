# createdNote

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The details of the note that you created.

**Availability**:
- iOS 11.0+ - Deprecated in 27.0
- iPadOS 11.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0
- watchOS 4.0+ - Deprecated in 27.0

> **Deprecated**: INCreateNoteIntentResponse is deprecated. Please adopt the Notes or Reminders AppSchema domain instead.

## Declaration

```swift
@NSCopying
var createdNote: INNote? { get set }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readwrite, nullable) INNote * createdNote;
```

*macOS*

```objc
@property (atomic, copy, readwrite, nullable) INNote * createdNote;
```

#### Discussion

Use this property to specify the content of the note that you created.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/increatenoteintentresponse/creatednote)*