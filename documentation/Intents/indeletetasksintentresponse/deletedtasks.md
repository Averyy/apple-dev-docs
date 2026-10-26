# deletedTasks

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

An array of tasks to delete.

**Availability**:
- iOS 13.0+ - Deprecated in 15.0
- iPadOS 13.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 6.0+ - Deprecated in 8.0

> **Deprecated**: This intent is no longer available. You may define a custom intent instead. For more information, see [Deprecated SiriKit Intent Domains](https://developer.apple.com/support/deprecated-sirikit-intent-domains).

## Declaration

```swift
var deletedTasks: [INTask]? { get set }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readwrite, nullable) NSArray<INTask *> * deletedTasks;
```

*macOS*

```objc
@property (atomic, copy, readwrite, nullable) NSArray<INTask *> * deletedTasks;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/indeletetasksintentresponse/deletedtasks)*