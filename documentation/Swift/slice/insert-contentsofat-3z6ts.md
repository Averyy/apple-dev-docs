# insert(contentsOf:at:)

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
mutating func insert<S>(contentsOf newElements: S, at i: Slice<Base>.Index) where S : Collection, Base.Element == S.Element
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/slice/insert(contentsof:at:)-3z6ts)*