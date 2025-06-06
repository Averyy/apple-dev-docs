# formUnion(_:)

**Framework**: FSKit  
**Kind**: method

Inserts the elements of another set into this option set.

**Availability**:
- macOS 15.4+

## Declaration

```swift
mutating func formUnion(_ other: Self)
```

#### Discussion

This method is implemented as a `|` (bitwise OR) operation on the two sets’ raw values.

## Parameters

- `other`: An option set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsvolume/itemdeactivationoptions/formunion(_:))*