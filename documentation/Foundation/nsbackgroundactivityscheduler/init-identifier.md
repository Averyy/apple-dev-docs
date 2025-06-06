# init(identifier:)

**Framework**: Foundation  
**Kind**: init

Initializes a background activity scheduler object with a specified unique identifier.

**Availability**:
- macOS 10.10+

## Declaration

```swift
init(identifier: String)
```

#### Return Value

A new background activity scheduler object of type [`NSBackgroundActivityScheduler`](nsbackgroundactivityscheduler.md).

#### Discussion

The string passed to the `identifier` parameter should remain constant for an activity across launches of your app because the system uses this unique identifier to track the number of times the activity has run and to improve the heuristics for deciding when to run it again in the future. See [`Create a Scheduler`](nsbackgroundactivityscheduler#Create-a-Scheduler.md).

## Parameters

- `identifier`: A unique string, in reverse DNS notation, that identifies the activity. For example,  .   and zero-length strings are not allowed.

## See Also

- [var identifier: String](nsbackgroundactivityscheduler/identifier.md)
  A unique reverse DNS notation string, such as `com.example.MyApp.updatecheck`, that identifies the activity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsbackgroundactivityscheduler/init(identifier:))*