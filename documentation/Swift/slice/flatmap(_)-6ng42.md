# flatMap(_:)

**Framework**: Swift  
**Kind**: method  
**Role**: Instance Method

Returns the non-`nil` results of mapping the given transformation over this sequence.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+
- Swift - Deprecated in 4.1 (renamed: compactMap(_:))

> **Deprecated**: Please use compactMap(_:) for the case where closure returns an optional value

## Declaration

```swift
func flatMap<ElementOfResult>(_ transform: @escaping (Self.Elements.Element) -> ElementOfResult?) -> LazyMapSequence<LazyFilterSequence<LazyMapSequence<Self.Elements, ElementOfResult?>>, ElementOfResult>
```

#### Discussion

Use this method to receive a sequence of non-optional values when your transformation produces an optional value.

> **Complexity**: O(1)

## Parameters

- `transform`: A closure that accepts an element of this sequence as its argument and returns an optional value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/slice/flatmap(_:)-6ng42)*