# beforeWaiting

**Framework**: Core Foundation  
**Kind**: property

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
static var beforeWaiting: CFRunLoopActivity { get }
```

#### Discussion

Inside the event processing loop before the run loop sleeps, waiting for a source or timer to fire. This activity does not occur if [`CFRunLoopRunInMode(_:_:_:)`](cfrunloopruninmode(_:_:_:).md) is called with a timeout of 0 seconds. It also does not occur in a particular iteration of the event processing loop if a version 0 source fires.

## See Also

- [static var entry: CFRunLoopActivity](cfrunloopactivity/entry.md)
  The entrance of the run loop, before entering the event processing loop. This activity occurs once for each call to [`CFRunLoopRun()`](cfrunlooprun().md) and [`CFRunLoopRunInMode(_:_:_:)`](cfrunloopruninmode(_:_:_:).md).
- [static var beforeTimers: CFRunLoopActivity](cfrunloopactivity/beforetimers.md)
  Inside the event processing loop before any timers are processed.
- [static var beforeSources: CFRunLoopActivity](cfrunloopactivity/beforesources.md)
  Inside the event processing loop before any sources are processed.
- [static var afterWaiting: CFRunLoopActivity](cfrunloopactivity/afterwaiting.md)
  Inside the event processing loop after the run loop wakes up, but before processing the event that woke it up. This activity occurs only if the run loop did in fact go to sleep during the current loop.
- [static var exit: CFRunLoopActivity](cfrunloopactivity/exit.md)
  The exit of the run loop, after exiting the event processing loop. This activity occurs once for each call to [`CFRunLoopRun()`](cfrunlooprun().md) and [`CFRunLoopRunInMode(_:_:_:)`](cfrunloopruninmode(_:_:_:).md).
- [static var allActivities: CFRunLoopActivity](cfrunloopactivity/allactivities.md)
  A combination of all the preceding stages.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfrunloopactivity/beforewaiting)*