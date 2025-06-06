# CFMachPortInvalidationCallBack

**Framework**: Core Foundation  
**Kind**: typealias

Callback invoked when a CFMachPort object is invalidated.

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
typealias CFMachPortInvalidationCallBack = (CFMachPort?, UnsafeMutableRawPointer?) -> Void
```

#### Discussion

Your callback should free any resources allocated for `port`.

You specify this callback with [`CFMachPortSetInvalidationCallBack(_:_:)`](cfmachportsetinvalidationcallback(_:_:).md).

## Parameters

- `port`: The CFMachPort object that has been invalidated.
- `info`: The   member of the   structure used when creating  .

## See Also

- [typealias CFMachPortCallBack](cfmachportcallback.md)
  Callback invoked to process a message received on a CFMachPort object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfmachportinvalidationcallback)*