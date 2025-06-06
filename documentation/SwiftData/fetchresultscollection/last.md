# last

**Framework**: SwiftData  
**Kind**: property

The last element of the collection.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
var last: Self.Element? { get }
```

#### Discussion

If the collection is empty, the value of this property is `nil`.

```swift
let numbers = [10, 20, 30, 40, 50]
if let lastNumber = numbers.last {
    print(lastNumber)
}
// Prints "50"
```

> **Note**: O(1)

O(1)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftdata/fetchresultscollection/last)*