# take()

**Framework**: Swift  
**Kind**: method

Takes the wrapped value being stored in this instance and returns it while also setting the instance to `nil`. If there is no value being stored in this instance, this returns `nil` instead.

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
mutating func take() -> Optional<Wrapped>
```

#### Return Value

The wrapped value being stored in this instance. If this instance is `nil`, returns `nil`.

#### Discussion

```swift
var numberOfShoes: Int? = 34

if let numberOfShoes = numberOfShoes.take() {
  print(numberOfShoes)
  // Prints "34"
}

print(numberOfShoes)
// Prints "nil"
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/optional/take())*