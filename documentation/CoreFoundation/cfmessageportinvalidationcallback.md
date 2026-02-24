# CFMessagePortInvalidationCallBack

**Framework**: Core Foundation  
**Kind**: typealias

Callback invoked when a CFMessagePort object is invalidated.

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
typealias CFMessagePortInvalidationCallBack = (CFMessagePort?, UnsafeMutableRawPointer?) -> Void
```

#### Discussion

Your callback should free any resources allocated for `ms`.

You specify this callback with [`CFMessagePortSetInvalidationCallBack(_:_:)`](cfmessageportsetinvalidationcallback(_:_:).md).

## Parameters

- `ms`: The message port that has been invalidated.
- `info`: The `info` member of the [`CFMessagePortContext`](cfmessageportcontext.md) structure that was used when creating `ms`, if `ms` is a local port; `NULL` if `ms` is a remote port.

## See Also

- [typealias CFMessagePortCallBack](cfmessageportcallback.md)
  Callback invoked to process a message received on a CFMessagePort object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfmessageportinvalidationcallback)*