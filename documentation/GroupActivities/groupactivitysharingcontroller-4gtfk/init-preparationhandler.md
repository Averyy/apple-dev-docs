# init(preparationHandler:)

**Framework**: Group Activities  
**Kind**: init

Initializes the SharePlay sharing controller with a closure that creates the activity object.

**Availability**:
- macOS 13.0+

## Declaration

```swift
@MainActor
init<ActivityType>(preparationHandler: @escaping () async throws -> ActivityType) where ActivityType : GroupActivity
```

#### Discussion

The initializer executes the closure asynchronously so that your app can present the view controller in a timely manner. Use this method when the creation of the [`GroupActivity`](groupactivity.md) object might take a significant amount of time.

## Parameters

- `preparationHandler`: A closure that takes no parameters and   returns the activity object.

## See Also

- [init<ActivityType>(ActivityType) throws](groupactivitysharingcontroller-4gtfk/init(_:).md)
  Initializes the sharing controller with the specified activity and type information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/groupactivities/groupactivitysharingcontroller-4gtfk/init(preparationhandler:))*