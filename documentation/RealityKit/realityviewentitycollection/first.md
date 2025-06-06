# first

**Framework**: RealityKit  
**Kind**: property

The first element of the collection.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- visionOS ?+

## Declaration

```swift
var first: Self.Element? { get }
```

#### Discussion

If the collection is empty, the value of this property is `nil`.

```None
let numbers = [10, 20, 30, 40, 50]
if let firstNumber = numbers.first {
    print(firstNumber)
}
// Prints "10"
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/realityviewentitycollection/first)*