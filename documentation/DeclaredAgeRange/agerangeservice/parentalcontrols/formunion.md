# formUnion(_:)

**Framework**: Declared Age Range  
**Kind**: method

Inserts the elements of another set into this option set.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)

## Declaration

```swift
mutating func formUnion(_ other: Self)
```

#### Discussion

This method is implemented as a `|` (bitwise OR) operation on the two sets’ raw values.

## Parameters

- `other`: An option set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/declaredagerange/agerangeservice/parentalcontrols/formunion(_:))*