# subscript(_:)

**Framework**: Create ML Components  
**Kind**: subscript

Accesses a contiguous range of windows.

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
subscript(bounds: Range<Int>) -> Slice<SlidingWindows<Scalar>> { get }
```

## Parameters

- `bounds`: A range of valid indices in the classification distribution.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/slidingwindows/subscript(_:)-26j7f)*