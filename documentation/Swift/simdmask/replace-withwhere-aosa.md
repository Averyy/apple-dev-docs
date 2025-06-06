# replace(with:where:)

**Framework**: Swift  
**Kind**: method

Replaces elements of this vector with elements of `other` in the lanes where `mask` is `true`.

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
mutating func replace(with other: SIMDMask<Storage>, where mask: SIMDMask<Storage>)
```

#### Discussion

Equivalent to:

```swift
for i in indices {
  if mask[i] { self[i] = other[i] }
}
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/simdmask/replace(with:where:)-aosa)*