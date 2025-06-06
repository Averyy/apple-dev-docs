# schedule

**Framework**: Core Foundation  
**Kind**: property

A scheduling callback for the run loop source. This callback is called when the source is added to a run loop mode. Can be `NULL`.

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
var schedule: ((UnsafeMutableRawPointer?, CFRunLoop?, CFRunLoopMode?) -> Void)!
```

## Parameters

- `info`: The   member of the   structure that was used when creating the run loop source.
- `rl`: The run loop in which the source is being scheduled.
- `mode`: The run loop mode in which the source is being scheduled.

## See Also

- [var cancel: ((UnsafeMutableRawPointer?, CFRunLoop?, CFRunLoopMode?) -> Void)!](cfrunloopsourcecontext/cancel.md)
- [var equal: ((UnsafeRawPointer?, UnsafeRawPointer?) -> DarwinBoolean)!](cfrunloopsourcecontext/equal.md)
  An equality test callback for your program-defined `info` pointer. Can be `NULL`.
- [var hash: ((UnsafeRawPointer?) -> CFHashCode)!](cfrunloopsourcecontext/hash.md)
  A hash calculation callback for your program-defined `info` pointer. Can be `NULL`.
- [var perform: ((UnsafeMutableRawPointer?) -> Void)!](cfrunloopsourcecontext/perform.md)
  A perform callback for the run loop source. This callback is called when the source has fired.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfrunloopsourcecontext/schedule)*