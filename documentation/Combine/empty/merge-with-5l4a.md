# merge(with:)

**Framework**: Combine  
**Kind**: method

Combines elements from this publisher with those from another publisher of the same type, delivering an interleaved sequence of elements.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
func merge(with other: Self) -> Publishers.MergeMany<Self>
```

#### Return Value

A publisher that emits an event when either upstream publisher emits an event.

## Parameters

- `other`: Another publisher of this publisher’s type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/empty/merge(with:)-5l4a)*