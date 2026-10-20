# init(repeating:)

**Framework**: Swift  
**Kind**: init  
**Role**: Initializer

A vector with the specified scalar in all lanes.

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
init(repeating scalar: Int)
```

Available when `Scalar` is `Int`.

#### Discussion

Equivalent to:

```swift
var result = SIMD64<Int>()
for i in result.indices {
  result[i] = scalar
}
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/simd64/init(repeating:)-6v9hc)*