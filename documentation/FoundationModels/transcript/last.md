# last

**Framework**: Foundation Models  
**Kind**: property

The last element of the collection.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
var last: Self.Element? { get }
```

#### Discussion

If the collection is empty, the value of this property is `nil`.

```None
let numbers = [10, 20, 30, 40, 50]
if let lastNumber = numbers.last {
    print(lastNumber)
}
// Prints "50"
```

> **Note**: O(1)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/transcript/last)*