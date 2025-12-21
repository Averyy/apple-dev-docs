# init(rawValue:)

**Framework**: RealityKit  
**Kind**: init

Creates a fill mode from its backing data type.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 26.0+
- visionOS ?+

## Declaration

```swift
init(rawValue: Int8)
```

#### Discussion

Use this initializer to unarchive a fill mode from data:

```swift
let rawValue = unarchiveNextInt8(from: data) // Pseudo code.
let fillMode = AnimationFillMode(rawValue: rawValue)
```

## Parameters

- `rawValue`: The backing data value for the fill mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/animationfillmode/init(rawvalue:))*