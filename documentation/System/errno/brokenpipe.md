# brokenPipe

**Framework**: System  
**Kind**: property

Broken pipe.

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
static var brokenPipe: Errno { get }
```

## Mentions

- [Adopting Swift Error Constants](adopting-errno.md)

#### Discussion

You attempted to write to a pipe, socket, or FIFO that doesn’t have a process reading its data.

The corresponding C error is `EPIPE`.

## See Also

- [static var illegalSeek: Errno](errno/illegalseek.md)
  Illegal seek.


---

*[View on Apple Developer](https://developer.apple.com/documentation/system/errno/brokenpipe)*