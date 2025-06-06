# append(contentsOf:)

**Framework**: Swift  
**Kind**: method

Appends the Unicode scalar values in the given sequence to the view.

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
mutating func append<S>(contentsOf newElements: S) where S : Sequence, S.Element == Unicode.Scalar
```

#### Discussion

> **Note**: O(), where  is the length of the resulting view.

## Parameters

- `newElements`: A sequence of Unicode scalar values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/string/unicodescalarview/append(contentsof:))*