# illegalSeek

**Framework**: System  
**Kind**: property

Illegal seek.

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
static var illegalSeek: Errno { get }
```

## Mentions

- [Adopting Swift Error Constants](adopting-errno.md)

#### Discussion

An `lseek(2)` function was issued on a socket, pipe or FIFO.

The corresponding C error is `ESPIPE`.

## See Also

- [static var brokenPipe: Errno](errno/brokenpipe.md)
  Broken pipe.


---

*[View on Apple Developer](https://developer.apple.com/documentation/system/errno/illegalseek)*