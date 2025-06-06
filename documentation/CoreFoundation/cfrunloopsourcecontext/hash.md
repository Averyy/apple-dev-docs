# hash

**Framework**: Core Foundation  
**Kind**: property

A hash calculation callback for your program-defined `info` pointer. Can be `NULL`.

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
var hash: ((UnsafeRawPointer?) -> CFHashCode)!
```

#### Return Value

A hash code value for `info`.

#### Discussion

If a hash callback is not provided for a source, the `info` pointer is used.

## Parameters

- `info`: The   member of the   or   structure that was used when creating the run loop source.

## See Also

- [var cancel: ((UnsafeMutableRawPointer?, CFRunLoop?, CFRunLoopMode?) -> Void)!](cfrunloopsourcecontext/cancel.md)
- [var equal: ((UnsafeRawPointer?, UnsafeRawPointer?) -> DarwinBoolean)!](cfrunloopsourcecontext/equal.md)
  An equality test callback for your program-defined `info` pointer. Can be `NULL`.
- [var perform: ((UnsafeMutableRawPointer?) -> Void)!](cfrunloopsourcecontext/perform.md)
  A perform callback for the run loop source. This callback is called when the source has fired.
- [var schedule: ((UnsafeMutableRawPointer?, CFRunLoop?, CFRunLoopMode?) -> Void)!](cfrunloopsourcecontext/schedule.md)
  A scheduling callback for the run loop source. This callback is called when the source is added to a run loop mode. Can be `NULL`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfrunloopsourcecontext/hash)*