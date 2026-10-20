# init(identifier:)

**Framework**: Foundation  
**Kind**: init  
**Role**: Initializer

Initializes a background activity scheduler object with a specified unique identifier.

**Availability**:
- macOS 10.10+

## Declaration

```swift
init(identifier: String)
```

```objc
- (instancetype) initWithIdentifier:(NSString *) identifier;
```

#### Return Value

A new background activity scheduler object of type [`NSBackgroundActivityScheduler`](../nsbackgroundactivityscheduler.md).

#### Discussion

The string passed to the `identifier` parameter should remain constant for an activity across launches of your app because the system uses this unique identifier to track the number of times the activity has run and to improve the heuristics for deciding when to run it again in the future. See [Create a Scheduler](../nsbackgroundactivityscheduler.md#Create-a-Scheduler).

## Parameters

- `identifier`: A unique string, in reverse DNS notation, that identifies the activity. For example, `com.example.MyApp.updatecheck`. `nil` and zero-length strings are not allowed.

## See Also

### Related Documentation
- [var identifier: String](./identifier.md)
  A unique reverse DNS notation string, such as `com.example.MyApp.updatecheck`, that identifies the activity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsbackgroundactivityscheduler/init(identifier:))*