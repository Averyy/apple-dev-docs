# init(_:)

**Framework**: Swift  
**Kind**: init

Creates a range set containing the values in the given ranges.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
init(_ ranges: some Sequence<Range<Bound>>)
```

#### Discussion

Any empty ranges in `ranges` are ignored, and non-empty ranges are merged to eliminate any overlaps. As such, the `ranges` collection in the resulting range set may not be equivalent to the sequence of ranges passed to this initializer.

## Parameters

- `ranges`: The ranges to use for the new range set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/rangeset/init(_:)-9x0yj)*