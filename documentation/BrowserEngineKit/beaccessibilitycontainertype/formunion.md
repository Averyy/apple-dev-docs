# formUnion(_:)

**Framework**: BrowserEngineKit  
**Kind**: method

Inserts the elements of another set into this option set.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
mutating func formUnion(_ other: Self)
```

#### Discussion

This method is implemented as a `|` (bitwise OR) operation on the two sets’ raw values.

## Parameters

- `other`: An option set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/beaccessibilitycontainertype/formunion(_:))*