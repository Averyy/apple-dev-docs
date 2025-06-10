# removeSubrange(_:)

**Framework**: MusicKit  
**Kind**: method

Removes the elements in the specified subrange from the collection.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
mutating func removeSubrange(_ bounds: Range<Self.Index>)
```

#### Discussion

All the elements following the specified position are moved to close the gap. This example removes three elements from the middle of an array of measurements.

```swift
var measurements = [1.2, 1.5, 2.9, 1.2, 1.5]
measurements.removeSubrange(1..<4)
print(measurements)
// Prints "[1.2, 1.5]"
```

Calling this method may invalidate any existing indices for use with this collection.

> **Note**: O(), where  is the length of the collection.

## Parameters

- `bounds`: The range of the collection to be removed. The   bounds of the range must be valid indices of the collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/musickit/applicationmusicplayer/queue-swift.class/entries-swift.struct/removesubrange(_:)-37gem)*