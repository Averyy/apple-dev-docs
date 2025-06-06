# noMemory

**Framework**: System  
**Kind**: property

Can’t allocate memory.

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
static var noMemory: Errno { get }
```

## Mentions

- [Adopting Swift Error Constants](adopting-errno.md)

#### Discussion

The new process image required more memory than was allowed by the hardware or by system-imposed memory management constraints. A lack of swap space is normally temporary; however, a lack of core is not. You can increase soft limits up to their corresponding hard limits.

The corresponding C error is `ENOMEM`.

## See Also

- [static var deadlock: Errno](errno/deadlock.md)
  Resource deadlock avoided.
- [static var wouldBlock: Errno](errno/wouldblock.md)
  Operation would block.


---

*[View on Apple Developer](https://developer.apple.com/documentation/system/errno/nomemory)*