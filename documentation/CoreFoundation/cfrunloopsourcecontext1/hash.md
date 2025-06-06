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


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfrunloopsourcecontext1/hash)*