# init(lowHalf:highHalf:)

**Framework**: Swift  
**Kind**: init

A vector formed by concatenating lowHalf and highHalf.

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
init(lowHalf: SIMD4<Float16>, highHalf: SIMD4<Float16>)
```

#### Discussion

Equivalent to:

```swift
var result = SIMD8<Float16>()
for i in 0..<4 {
  result[i] = lowHalf[i]
  result[4+i] = highHalf[i]
}
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/simd8/init(lowhalf:highhalf:)-40zc3)*