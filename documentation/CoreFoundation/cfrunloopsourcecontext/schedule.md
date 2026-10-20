# schedule

**Framework**: Core Foundation  
**Kind**: property  
**Role**: Instance Property

A scheduling callback for the run loop source. This callback is called when the source is added to a run loop mode. Can be `NULL`.

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
var schedule: ((UnsafeMutableRawPointer?, CFRunLoop?, CFRunLoopMode?) -> Void)!
```

```c
void (*)(void *, struct __CFRunLoop *, const struct __CFString *) schedule;
```

## Parameters

- `info`: The `info` member of the [`CFRunLoopSourceContext`](../cfrunloopsourcecontext.md) structure that was used when creating the run loop source.
- `rl`: The run loop in which the source is being scheduled.
- `mode`: The run loop mode in which the source is being scheduled.

## See Also

### Callbacks
- [var cancel: ((UnsafeMutableRawPointer?, CFRunLoop?, CFRunLoopMode?) -> Void)!](./cancel.md)
- [var equal: ((UnsafeRawPointer?, UnsafeRawPointer?) -> DarwinBoolean)!](./equal.md)
  An equality test callback for your program-defined `info` pointer. Can be `NULL`.
- [var hash: ((UnsafeRawPointer?) -> CFHashCode)!](./hash.md)
  A hash calculation callback for your program-defined `info` pointer. Can be `NULL`.
- [var perform: ((UnsafeMutableRawPointer?) -> Void)!](./perform.md)
  A perform callback for the run loop source. This callback is called when the source has fired.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfrunloopsourcecontext/schedule)*