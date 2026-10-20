# beforeSources

**Framework**: Core Foundation  
**Kind**: property  
**Role**: Type Property

Inside the event processing loop before any sources are processed.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
static var beforeSources: CFRunLoopActivity { get }
```

```c
kCFRunLoopBeforeSources
```

## See Also

### Constants
- [static var entry: CFRunLoopActivity](./entry.md)
  The entrance of the run loop, before entering the event processing loop. This activity occurs once for each call to [`CFRunLoopRun()`](../cfrunlooprun%28%29.md) and [`CFRunLoopRunInMode(_:_:_:)`](../cfrunloopruninmode%28_,_,_%29.md).
- [static var beforeTimers: CFRunLoopActivity](./beforetimers.md)
  Inside the event processing loop before any timers are processed.
- [static var beforeWaiting: CFRunLoopActivity](./beforewaiting.md)
- [static var afterWaiting: CFRunLoopActivity](./afterwaiting.md)
  Inside the event processing loop after the run loop wakes up, but before processing the event that woke it up. This activity occurs only if the run loop did in fact go to sleep during the current loop.
- [static var exit: CFRunLoopActivity](./exit.md)
  The exit of the run loop, after exiting the event processing loop. This activity occurs once for each call to [`CFRunLoopRun()`](../cfrunlooprun%28%29.md) and [`CFRunLoopRunInMode(_:_:_:)`](../cfrunloopruninmode%28_,_,_%29.md).
- [static var allActivities: CFRunLoopActivity](./allactivities.md)
  A combination of all the preceding stages.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfrunloopactivity/beforesources)*