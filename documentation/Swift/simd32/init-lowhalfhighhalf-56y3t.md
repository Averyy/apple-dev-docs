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
init(lowHalf: SIMD16<Float16>, highHalf: SIMD16<Float16>)
```

#### Discussion

Equivalent to:

```swift
var result = SIMD32<Float16>()
for i in 0..<16 {
  result[i] = lowHalf[i]
  result[16+i] = highHalf[i]
}
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/simd32/init(lowhalf:highhalf:)-56y3t)*