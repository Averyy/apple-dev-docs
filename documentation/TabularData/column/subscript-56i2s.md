# subscript(_:)

**Framework**: TabularData  
**Kind**: subscript

Returns a column slice that includes elements that correspond to a collection of Booleans.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
subscript<C>(mask: C) -> DiscontiguousColumnSlice<WrappedElement> where C : Collection, C.Element == Bool { get }
```

#### Overview

You can create a Boolean column for this subscript by comparing a column to a value of the column elements’ type.

```swift
let followerColumn = artists["Followers", Int.self].filled(with: 0)
let popularArtists = artists[followerColumn > 10_000_000]
```

## Parameters

- `mask`: A Boolean collection. The subscript returns a slice that includes the column elements   that correspond to the   elements in  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/column/subscript(_:)-56i2s)*