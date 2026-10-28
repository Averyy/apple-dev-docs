# subscript(_:)

**Framework**: Create ML Components  
**Kind**: subscript  
**Role**: Instance Subscript

Accesses a probability with label.

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
subscript(label: Label) -> Float? { get }
```

**Other overloads**:

```swift
subscript(bounds: Range<Int>) -> Slice<ClassificationDistribution<Label>> { get }
```

```swift
subscript(index: Int) -> Classification<Label> { get }
```

## Parameters

- `label`: A label in the classification set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/classificationdistribution/subscript(_:)-s5as)*