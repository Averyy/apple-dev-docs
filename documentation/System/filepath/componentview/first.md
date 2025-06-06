# first

**Framework**: System  
**Kind**: property

The first element of the collection.

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

*[View on Apple Developer](https://developer.apple.com/documentation/system/filepath/componentview/first)*