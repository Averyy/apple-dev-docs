# subscript(_:)

**Framework**: Create ML Components  
**Kind**: subscript  
**Role**: Instance Subscript

Accesses a classification at an index.

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
subscript(index: Int) -> Classification<Label> { get }
```

**Other overloads**:

```swift
subscript(bounds: Range<Int>) -> Slice<ClassificationDistribution<Label>> { get }
```

```swift
subscript(label: Label) -> Float? { get }
```

## Parameters

- `index`: A valid index to a classification in the classification distribution.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/classificationdistribution/subscript(_:)-856r7)*