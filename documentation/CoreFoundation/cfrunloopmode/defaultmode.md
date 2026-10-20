# defaultMode

**Framework**: Core Foundation  
**Kind**: property  
**Role**: Type Property

Run loop mode that should be used when a thread is in its default, or idle, state, waiting for an event. This mode is used when the run loop is started with [`CFRunLoopRun()`](../cfrunlooprun%28%29.md).

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
static let defaultMode: CFRunLoopMode!
```

```c
extern CFRunLoopMode const kCFRunLoopDefaultMode;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfrunloopmode/defaultmode)*