# createdDateComponents

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The initial creation date of the task.

**Availability**:
- iOS 11.0+ - Deprecated in 27.0
- iPadOS 11.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0
- watchOS 4.0+ - Deprecated in 27.0

> **Deprecated**: INTask is deprecated. Please adopt the Notes or Reminders AppSchema domain instead.

## Declaration

```swift
var createdDateComponents: DateComponents? { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readonly, nullable) NSDateComponents * createdDateComponents;
```

*macOS*

```objc
@property (atomic, copy, readonly, nullable) NSDateComponents * createdDateComponents;
```

## See Also

### Getting the Modification Dates
- [var modifiedDateComponents: DateComponents?](./modifieddatecomponents.md)
  The date on which the intent updated the task.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/intask/createddatecomponents)*