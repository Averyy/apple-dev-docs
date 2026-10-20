# init(_:)

**Framework**: Group Activities  
**Kind**: init  
**Role**: Initializer

Initializes the sharing controller with the specified activity and type information.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 15.4+
- visionOS 1.0+

## Declaration

```swift
@MainActor
init<ActivityType>(_ activity: ActivityType) throws where ActivityType : GroupActivity
```

## Parameters

- `activity`: The activity object to start.

## See Also

### Creating the group activity sharing controller
- [init<ActivityType>(preparationHandler: () async throws -> ActivityType)](./init%28preparationhandler%29.md)
  Initializes the SharePlay sharing controller with a closure that creates the activity object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/groupactivities/groupactivitysharingcontroller-ybcy/init(_:))*