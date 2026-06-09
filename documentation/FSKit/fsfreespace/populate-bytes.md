# populate(bytes:)

**Framework**: FSKit  
**Kind**: method

Populates this instance with the given free space value and atomically assigns a sequence number.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
func populate(bytes freeSpaceBytes: UInt64)
```

#### Discussion

> ❗ **Important**:  FSKit uses internal sequencing technology within this method to determine the most up-to-date free space of the volume. To ensure correctness, call this method within an isolation context covering the volume’s free space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsfreespace/populate(bytes:))*