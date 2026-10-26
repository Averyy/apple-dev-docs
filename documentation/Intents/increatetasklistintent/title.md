# title

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The title of the task list.

**Availability**:
- iOS 11.0+ - Deprecated in 15.0
- iPadOS 11.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 4.0+ - Deprecated in 8.0

> **Deprecated**: This intent is no longer available. You may define a custom intent instead. For more information, see [Deprecated SiriKit Intent Domains](https://developer.apple.com/support/deprecated-sirikit-intent-domains).

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

## See Also

### Getting the Task List Details
- [var taskTitles: [INSpeakableString]?](./tasktitles.md)
  An array of strings containing the titles for individual tasks to add to the new task list.
- [var groupName: INSpeakableString?](./groupname.md)
  The group that contains the task list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/increatetasklistintent/title)*