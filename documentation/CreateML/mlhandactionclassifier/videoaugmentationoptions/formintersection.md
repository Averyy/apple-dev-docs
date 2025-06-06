# formIntersection(_:)

**Framework**: Create ML  
**Kind**: method

Removes all elements of this option set that are not also present in the given set.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.14+
- visionOS 1.0+

## Declaration

```swift
mutating func formIntersection(_ other: Self)
```

#### Discussion

This method is implemented as a `&` (bitwise AND) operation on the two sets’ raw values.

## Parameters

- `other`: An option set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlhandactionclassifier/videoaugmentationoptions/formintersection(_:))*