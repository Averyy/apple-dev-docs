# CFRunLoopObserverCallBack

**Framework**: Core Foundation  
**Kind**: typealias

Callback invoked when a CFRunLoopObserver object is fired.

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
typealias CFRunLoopObserverCallBack = (CFRunLoopObserver?, CFRunLoopActivity, UnsafeMutableRawPointer?) -> Void
```

#### Discussion

You specify this callback when you create the run loop observer with [`CFRunLoopObserverCreate(_:_:_:_:_:_:)`](cfrunloopobservercreate(_:_:_:_:_:_:).md).

## Parameters

- `observer`: The run loop observer that is firing.
- `activity`: The current activity stage of the run loop.
- `info`: The   member of the   structure that was used when creating the run loop observer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfrunloopobservercallback)*