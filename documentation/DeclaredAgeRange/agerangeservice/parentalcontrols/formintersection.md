# formIntersection(_:)

**Framework**: Declared Age Range  
**Kind**: method

Removes all elements of this option set that are not also present in the given set.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)

## Declaration

```swift
mutating func formIntersection(_ other: Self)
```

#### Discussion

This method is implemented as a `&` (bitwise AND) operation on the two sets’ raw values.

## Parameters

- `other`: An option set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/declaredagerange/agerangeservice/parentalcontrols/formintersection(_:))*