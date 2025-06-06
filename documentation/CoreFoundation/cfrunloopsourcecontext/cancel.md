# cancel

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
var cancel: ((UnsafeMutableRawPointer?, CFRunLoop?, CFRunLoopMode?) -> Void)!
```

#### Discussion

A cancel callback for the run loop source. This callback is called when the source is removed from a run loop mode. Can be `NULL`.

## Parameters

- `info`: The   member of the   structure that was used when creating the run loop source.
- `rl`: The run loop from which the run loop source is being removed.
- `mode`: The run loop mode from which the run loop source is being removed.

## See Also

- [var equal: ((UnsafeRawPointer?, UnsafeRawPointer?) -> DarwinBoolean)!](cfrunloopsourcecontext/equal.md)
  An equality test callback for your program-defined `info` pointer. Can be `NULL`.
- [var hash: ((UnsafeRawPointer?) -> CFHashCode)!](cfrunloopsourcecontext/hash.md)
  A hash calculation callback for your program-defined `info` pointer. Can be `NULL`.
- [var perform: ((UnsafeMutableRawPointer?) -> Void)!](cfrunloopsourcecontext/perform.md)
  A perform callback for the run loop source. This callback is called when the source has fired.
- [var schedule: ((UnsafeMutableRawPointer?, CFRunLoop?, CFRunLoopMode?) -> Void)!](cfrunloopsourcecontext/schedule.md)
  A scheduling callback for the run loop source. This callback is called when the source is added to a run loop mode. Can be `NULL`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfrunloopsourcecontext/cancel)*