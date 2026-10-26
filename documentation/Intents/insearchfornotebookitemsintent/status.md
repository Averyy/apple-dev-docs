# status

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The completion state to look for when searching for tasks.

**Availability**:
- iOS 11.0+ - Deprecated in 27.0
- iPadOS 11.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0
- watchOS 4.0+ - Deprecated in 27.0

> **Deprecated**: INSearchForNotebookItemsIntent is deprecated. Please adopt the Notes or Reminders AppSchema domain instead.

## Declaration

```swift
var status: INTaskStatus { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, assign, readonly) INTaskStatus status;
```

*macOS*

```objc
@property (atomic, assign, readonly) INTaskStatus status;
```

#### Discussion

When the value of this property is [`INTaskStatus.unknown`](../intaskstatus/unknown.md), don’t consider the status of a task when performing your search. For other values, include tasks in your search results only when their status matches the specified value.

## See Also

### Searching for Tasks by Their Status
- [enum INTaskStatus](../intaskstatus.md)
  Constants indicating the completion state of a task.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insearchfornotebookitemsintent/status)*