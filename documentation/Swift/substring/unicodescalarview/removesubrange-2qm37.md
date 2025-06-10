# removeSubrange(_:)

**Framework**: Swift  
**Kind**: method

Removes the elements in the specified subrange from the collection.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
mutating func removeSubrange<R>(_ bounds: R) where R : RangeExpression, Self.Index == R.Bound
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

*[View on Apple Developer](https://developer.apple.com/documentation/swift/substring/unicodescalarview/removesubrange(_:)-2qm37)*