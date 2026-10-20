# isStarted

**Framework**: ClassKit  
**Kind**: property  
**Role**: Instance Property

A Boolean that indicates whether an activity is running.

**Availability**:
- iOS 11.3+
- iPadOS 11.3+
- Mac Catalyst 11.3+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var isStarted: Bool { get }
```

```objc
@property (nonatomic, assign, readonly, getter=isStarted) BOOL started;
```

## See Also

### Starting and stopping an activity
- [func start()](./start%28%29.md)
  Tells an activity to start recording duration and progress for a task.
- [func stop()](./stop%28%29.md)
  Tells an activity to stop or pause recording duration and progress for a task.
- [var duration: TimeInterval](./duration.md)
  The cumulative time in seconds that an activity has been active.


---

*[View on Apple Developer](https://developer.apple.com/documentation/classkit/clsactivity/isstarted)*