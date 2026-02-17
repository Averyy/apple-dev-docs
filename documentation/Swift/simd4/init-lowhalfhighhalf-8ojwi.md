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
init(lowHalf: SIMD2<Float16>, highHalf: SIMD2<Float16>)
```

#### Discussion

Equivalent to:

```swift
var result = SIMD4<Float16>()
for i in 0..<2 {
  result[i] = lowHalf[i]
  result[2+i] = highHalf[i]
}
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/simd4/init(lowhalf:highhalf:)-8ojwi)*