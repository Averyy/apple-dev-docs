# CFRunLoopActivity

**Framework**: Core Foundation  
**Kind**: struct  
**Role**: Structure

Run loop activity stages in which run loop observers can be scheduled.

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
struct CFRunLoopActivity
```

```c
enum CFRunLoopActivity : CFOptionFlags;
```

## Overview

The run loop stages in which an observer is scheduled are selected when the observer is created with [`CFRunLoopObserverCreate(_:_:_:_:_:_:)`](./cfrunloopobservercreate%28_,_,_,_,_,_%29.md).

## Topics

### Constants
- [static var entry: CFRunLoopActivity](./cfrunloopactivity/entry.md)
  The entrance of the run loop, before entering the event processing loop. This activity occurs once for each call to [`CFRunLoopRun()`](./cfrunlooprun%28%29.md) and [`CFRunLoopRunInMode(_:_:_:)`](./cfrunloopruninmode%28_,_,_%29.md).
- [static var beforeTimers: CFRunLoopActivity](./cfrunloopactivity/beforetimers.md)
  Inside the event processing loop before any timers are processed.
- [static var beforeSources: CFRunLoopActivity](./cfrunloopactivity/beforesources.md)
  Inside the event processing loop before any sources are processed.
- [static var beforeWaiting: CFRunLoopActivity](./cfrunloopactivity/beforewaiting.md)
- [static var afterWaiting: CFRunLoopActivity](./cfrunloopactivity/afterwaiting.md)
  Inside the event processing loop after the run loop wakes up, but before processing the event that woke it up. This activity occurs only if the run loop did in fact go to sleep during the current loop.
- [static var exit: CFRunLoopActivity](./cfrunloopactivity/exit.md)
  The exit of the run loop, after exiting the event processing loop. This activity occurs once for each call to [`CFRunLoopRun()`](./cfrunlooprun%28%29.md) and [`CFRunLoopRunInMode(_:_:_:)`](./cfrunloopruninmode%28_,_,_%29.md).
- [static var allActivities: CFRunLoopActivity](./cfrunloopactivity/allactivities.md)
  A combination of all the preceding stages.
### Initializers
- [init(rawValue: CFOptionFlags)](./cfrunloopactivity/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../Swift/optionset.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [SetAlgebra](../Swift/setalgebra.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfrunloopactivity)*