# subscript(_:)

**Framework**: Create ML Components  
**Kind**: subscript

Accesses a contiguous range of elements.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 11.0+

## Declaration

```swift
subscript(bounds: Range<Int>) -> Slice<ClassificationDistribution<Label>> { get }
```

## Parameters

- `bounds`: A range of valid indices in the classification distribution.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/classificationdistribution/subscript(_:))*