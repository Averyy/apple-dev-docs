# insert(integersIn:)

**Framework**: Foundation  
**Kind**: method

Insert a range of integers into the `IndexSet`.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
mutating func insert<R>(integersIn range: R) where R : RangeExpression, R.Bound == Int
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/indexset/insert(integersin:)-9wcrp)*