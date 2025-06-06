# reserveCapacity(_:)

**Framework**: System  
**Kind**: method

Prepares the collection to store the specified number of elements, when doing so is appropriate for the underlying type.

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
mutating func reserveCapacity(_ n: Int)
```

#### Discussion

If you will be adding a known number of elements to a collection, use this method to avoid multiple reallocations. A type that conforms to `RangeReplaceableCollection` can choose how to respond when this method is called. Depending on the type, it may make sense to allocate more or less storage than requested or to take no action at all.

## Parameters

- `n`: The requested number of elements to store.


---

*[View on Apple Developer](https://developer.apple.com/documentation/system/filepath/componentview/reservecapacity(_:))*