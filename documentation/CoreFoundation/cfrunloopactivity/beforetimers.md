# beforeTimers

**Framework**: Core Foundation  
**Kind**: property

Inside the event processing loop before any timers are processed.

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
static var beforeTimers: CFRunLoopActivity { get }
```

## See Also

- [static var entry: CFRunLoopActivity](cfrunloopactivity/entry.md)
  The entrance of the run loop, before entering the event processing loop. This activity occurs once for each call to [`CFRunLoopRun()`](cfrunlooprun().md) and [`CFRunLoopRunInMode(_:_:_:)`](cfrunloopruninmode(_:_:_:).md).
- [static var beforeSources: CFRunLoopActivity](cfrunloopactivity/beforesources.md)
  Inside the event processing loop before any sources are processed.
- [static var beforeWaiting: CFRunLoopActivity](cfrunloopactivity/beforewaiting.md)
- [static var afterWaiting: CFRunLoopActivity](cfrunloopactivity/afterwaiting.md)
  Inside the event processing loop after the run loop wakes up, but before processing the event that woke it up. This activity occurs only if the run loop did in fact go to sleep during the current loop.
- [static var exit: CFRunLoopActivity](cfrunloopactivity/exit.md)
  The exit of the run loop, after exiting the event processing loop. This activity occurs once for each call to [`CFRunLoopRun()`](cfrunlooprun().md) and [`CFRunLoopRunInMode(_:_:_:)`](cfrunloopruninmode(_:_:_:).md).
- [static var allActivities: CFRunLoopActivity](cfrunloopactivity/allactivities.md)
  A combination of all the preceding stages.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfrunloopactivity/beforetimers)*