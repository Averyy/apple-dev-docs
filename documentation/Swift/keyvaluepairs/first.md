# first

**Framework**: Swift  
**Kind**: property

The first element of the collection.

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
var first: Self.Element? { get }
```

#### Discussion

If the collection is empty, the value of this property is `nil`.

```swift
let numbers = [10, 20, 30, 40, 50]
if let firstNumber = numbers.first {
    print(firstNumber)
}
// Prints "10"
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/keyvaluepairs/first)*