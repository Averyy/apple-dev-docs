# description

**Framework**: System  
**Kind**: property

A textual representation of the most recent error returned by a system call.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
var description: String { get }
```

#### Discussion

The corresponding C function is `strerror(3)`.

## See Also

- [var debugDescription: String](errno/debugdescription.md)
  A textual representation, suitable for debugging, of the most recent error returned by a system call.


---

*[View on Apple Developer](https://developer.apple.com/documentation/system/errno/description)*