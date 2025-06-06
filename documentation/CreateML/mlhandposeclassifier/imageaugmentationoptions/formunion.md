# formUnion(_:)

**Framework**: Create ML  
**Kind**: method

Inserts the elements of another set into this option set.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.14+
- visionOS 1.0+

## Declaration

```swift
mutating func formUnion(_ other: Self)
```

#### Discussion

This method is implemented as a `|` (bitwise OR) operation on the two sets’ raw values.

## Parameters

- `other`: An option set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlhandposeclassifier/imageaugmentationoptions/formunion(_:))*