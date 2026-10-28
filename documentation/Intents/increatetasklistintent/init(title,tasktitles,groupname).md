# init(title:taskTitles:groupName:)

**Framework**: Intents  
**Kind**: init  
**Role**: Initializer

Initializes the intent object with the specified task list details.

**Availability**:
- iOS 11.0+ - Deprecated in 15.0
- iPadOS 11.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 4.0+ - Deprecated in 8.0

> **Deprecated**: This intent is no longer available. You may define a custom intent instead. For more information, see [Deprecated SiriKit Intent Domains](https://developer.apple.com/support/deprecated-sirikit-intent-domains).

## Declaration

```swift
init(title: INSpeakableString?, taskTitles: [INSpeakableString]?, groupName: INSpeakableString?)
```

```objc
- (instancetype) initWithTitle:(INSpeakableString *) title taskTitles:(NSArray<INSpeakableString *> *) taskTitles groupName:(INSpeakableString *) groupName;
```

## Return Value

An initialized intent object or `nil` if the object could not be created.

## Discussion

Normally, you don’t create instances of this class yourself. Instead, SiriKit creates instances when the user asks to create a task list. However, you can use this method during testing to create intent objects in order to validate your intent handling code paths.

## Parameters

- `title`: The title of the task list.
- `taskTitles`: An array of strings containing the titles of any tasks to place in the task list.
- `groupName`: The name of the group in which to store the task list. Group names correspond to folders or other means of organizing task lists within your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/increatetasklistintent/init(title:tasktitles:groupname:))*