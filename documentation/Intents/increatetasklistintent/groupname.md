# groupName

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The group that contains the task list.

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

Use groups to organize task lists within your app. A group might correspond to a folder that contains related task lists. For example, the Reminders app uses groups to manage the task lists for different services. The group name should correspond to the user-visible name of the group in your app.

## See Also

### Getting the Task List Details
- [var title: INSpeakableString?](./title.md)
  The title of the task list.
- [var taskTitles: [INSpeakableString]?](./tasktitles.md)
  An array of strings containing the titles for individual tasks to add to the new task list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/increatetasklistintent/groupname)*