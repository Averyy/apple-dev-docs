# first

**Framework**: Foundation Models  
**Kind**: property

The first element of the collection.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

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

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/transcript/toolcalls/first)*