# init(activityType:)

**Framework**: Foundation  
**Kind**: init

Creates a user activity object with the specified type.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
init(activityType: String)
```

#### Return Value

An [`NSUserActivity`](nsuseractivity.md) object.

## Parameters

- `activityType`: The type of the activity. The value is a developer-defined string in reverse-DNS format by convention, for example,  .

## See Also

- [Handoff Programming Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/Handoff/HandoffFundamentals/HandoffFundamentals.html#//apple_ref/doc/uid/TP40014338)
- [Creating a user activity object](creating-a-user-activity-object.md)
  Identify key user interactions and include the information to restore them later.
- [convenience init()](nsuseractivity/init.md)
  Creates a user activity object using the first activity type declared in the app’s information property list file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsuseractivity/init(activitytype:))*