# modifiedDateComponents

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The date on which the intent most recently modified the note.

**Availability**:
- iOS 11.0+ - Deprecated in 27.0
- iPadOS 11.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0
- watchOS 4.0+ - Deprecated in 27.0

> **Deprecated**: INNote is deprecated. Please adopt the Notes or Reminders AppSchema domain instead.

## Declaration

```swift
var modifiedDateComponents: DateComponents? { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readonly, nullable) NSDateComponents * modifiedDateComponents;
```

*macOS*

```objc
@property (atomic, copy, readonly, nullable) NSDateComponents * modifiedDateComponents;
```

## See Also

### Getting the Modification Dates
- [var createdDateComponents: DateComponents?](./createddatecomponents.md)
  The creation date of the note.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/innote/modifieddatecomponents)*