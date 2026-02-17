# init(repeating:)

**Framework**: Swift  
**Kind**: init

A vector with the specified scalar in all lanes.

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
init(repeating scalar: Float16)
```

#### Discussion

Equivalent to:

```swift
var result = SIMD8<Float16>()
for i in result.indices {
  result[i] = scalar
}
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/simd8/init(repeating:)-5u1bp)*