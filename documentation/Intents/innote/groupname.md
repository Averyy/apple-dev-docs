# groupName

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The user-visible name of the group that contains the note.

**Availability**:
- iOS 11.0+ - Deprecated in 27.0
- iPadOS 11.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0
- watchOS 4.0+ - Deprecated in 27.0

> **Deprecated**: INNote is deprecated. Please adopt the Notes or Reminders AppSchema domain instead.

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

## Discussion

Use groups to organize notes within your app. For example, you might use this property to specify the name of the folder containing the note. Group names should always correspond to the user-visible name of the container, and not to any internal designation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/innote/groupname)*