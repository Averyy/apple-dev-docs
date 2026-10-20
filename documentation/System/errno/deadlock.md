# deadlock

**Framework**: System  
**Kind**: property  
**Role**: Type Property

Resource deadlock avoided.

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
static var deadlock: Errno { get }
```

## Mentions

- [Adopting Swift Error Constants](../adopting-errno.md)

#### Discussion

You attempted to lock a system resource that would have resulted in a deadlock.

The corresponding C error is `EDEADLK`.

## See Also

### Runtime Errors
- [static var noMemory: Errno](./nomemory.md)
  Can’t allocate memory.
- [static var wouldBlock: Errno](./wouldblock.md)
  Operation would block.


---

*[View on Apple Developer](https://developer.apple.com/documentation/system/errno/deadlock)*