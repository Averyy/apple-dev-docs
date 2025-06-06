# replaceSubrange(_:with:)

**Framework**: Swift  
**Kind**: method

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
mutating func replaceSubrange<C>(_ subRange: Range<Slice<Base>.Index>, with newElements: C) where C : Collection, Base.Element == C.Element
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/slice/replacesubrange(_:with:)-904p8)*