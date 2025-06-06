# wouldBlock

**Framework**: System  
**Kind**: property

Operation would block.

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
static var wouldBlock: Errno { get }
```

## Mentions

- [Adopting Swift Error Constants](adopting-errno.md)

#### Discussion

The corresponding C error is `EWOULDBLOCK`.

## See Also

- [static var deadlock: Errno](errno/deadlock.md)
  Resource deadlock avoided.
- [static var noMemory: Errno](errno/nomemory.md)
  Can’t allocate memory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/system/errno/wouldblock)*