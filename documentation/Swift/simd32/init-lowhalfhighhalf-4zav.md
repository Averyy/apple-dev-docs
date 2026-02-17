# init(lowHalf:highHalf:)

**Framework**: Swift  
**Kind**: init

A vector formed by concatenating lowHalf and highHalf.

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
init(lowHalf: SIMD16<UInt32>, highHalf: SIMD16<UInt32>)
```

#### Discussion

Equivalent to:

```swift
var result = SIMD32<UInt32>()
for i in 0..<16 {
  result[i] = lowHalf[i]
  result[16+i] = highHalf[i]
}
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/simd32/init(lowhalf:highhalf:)-4zav)*