# beforeWaiting

**Framework**: Core Foundation  
**Kind**: property  
**Role**: Type Property

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
static var beforeWaiting: CFRunLoopActivity { get }
```

```c
kCFRunLoopBeforeWaiting
```

## Discussion

Inside the event processing loop before the run loop sleeps, waiting for a source or timer to fire. This activity does not occur if [`CFRunLoopRunInMode(_:_:_:)`](../cfrunloopruninmode%28_,_,_%29.md) is called with a timeout of 0 seconds. It also does not occur in a particular iteration of the event processing loop if a version 0 source fires.

## See Also

### Constants
- [static var entry: CFRunLoopActivity](./entry.md)
  The entrance of the run loop, before entering the event processing loop. This activity occurs once for each call to [`CFRunLoopRun()`](../cfrunlooprun%28%29.md) and [`CFRunLoopRunInMode(_:_:_:)`](../cfrunloopruninmode%28_,_,_%29.md).
- [static var beforeTimers: CFRunLoopActivity](./beforetimers.md)
  Inside the event processing loop before any timers are processed.
- [static var beforeSources: CFRunLoopActivity](./beforesources.md)
  Inside the event processing loop before any sources are processed.
- [static var afterWaiting: CFRunLoopActivity](./afterwaiting.md)
  Inside the event processing loop after the run loop wakes up, but before processing the event that woke it up. This activity occurs only if the run loop did in fact go to sleep during the current loop.
- [static var exit: CFRunLoopActivity](./exit.md)
  The exit of the run loop, after exiting the event processing loop. This activity occurs once for each call to [`CFRunLoopRun()`](../cfrunlooprun%28%29.md) and [`CFRunLoopRunInMode(_:_:_:)`](../cfrunloopruninmode%28_,_,_%29.md).
- [static var allActivities: CFRunLoopActivity](./allactivities.md)
  A combination of all the preceding stages.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfrunloopactivity/beforewaiting)*