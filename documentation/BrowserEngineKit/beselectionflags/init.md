# init(_:)

**Framework**: BrowserEngineKit  
**Kind**: init

Creates a new set from a finite sequence of items.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
init<S>(_ sequence: S) where S : Sequence, Self.Element == S.Element
```

#### Discussion

Use this initializer to create a new set from an existing sequence, like an array or a range:

```None
let validIndices = Set(0..<7).subtracting([2, 4, 5])
print(validIndices)
// Prints "[6, 0, 1, 3]"
```

## Parameters

- `sequence`: The elements to use as members of the new set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/beselectionflags/init(_:))*