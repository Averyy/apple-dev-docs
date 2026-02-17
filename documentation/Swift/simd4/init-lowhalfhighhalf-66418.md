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
init(lowHalf: SIMD2<Double>, highHalf: SIMD2<Double>)
```

#### Discussion

Equivalent to:

```swift
var result = SIMD4<Double>()
for i in 0..<2 {
  result[i] = lowHalf[i]
  result[2+i] = highHalf[i]
}
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/simd4/init(lowhalf:highhalf:)-66418)*