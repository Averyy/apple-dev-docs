# equal

**Framework**: Core Foundation  
**Kind**: property  
**Role**: Instance Property

An equality test callback for your program-defined `info` pointer. Can be `NULL`.

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
var equal: ((UnsafeRawPointer?, UnsafeRawPointer?) -> DarwinBoolean)!
```

```c
unsigned char (*)(const void *, const void *) equal;
```

#### Return Value

`true` if `info1` and `info2` should be considered equal; otherwise `false`.

#### Discussion

An equality test callback for your program-defined `info` pointer. Can be `NULL`.

## Parameters

- `info1`: The `info` member of the [`CFRunLoopSourceContext`](../cfrunloopsourcecontext.md) or [`CFRunLoopSourceContext1`](../cfrunloopsourcecontext1.md) structure that was used when creating the first run loop source to test.
- `info2`: The `info` member of the [`CFRunLoopSourceContext`](../cfrunloopsourcecontext.md) or [`CFRunLoopSourceContext1`](../cfrunloopsourcecontext1.md) structure that was used when creating the second run loop source to test.

## See Also

### Callbacks
- [var cancel: ((UnsafeMutableRawPointer?, CFRunLoop?, CFRunLoopMode?) -> Void)!](./cancel.md)
- [var hash: ((UnsafeRawPointer?) -> CFHashCode)!](./hash.md)
  A hash calculation callback for your program-defined `info` pointer. Can be `NULL`.
- [var perform: ((UnsafeMutableRawPointer?) -> Void)!](./perform.md)
  A perform callback for the run loop source. This callback is called when the source has fired.
- [var schedule: ((UnsafeMutableRawPointer?, CFRunLoop?, CFRunLoopMode?) -> Void)!](./schedule.md)
  A scheduling callback for the run loop source. This callback is called when the source is added to a run loop mode. Can be `NULL`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfrunloopsourcecontext/equal)*