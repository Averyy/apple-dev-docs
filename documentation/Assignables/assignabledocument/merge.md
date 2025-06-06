# merge(_:)

**Framework**: Assignables  
**Kind**: method

Merge another object of this type into this object.

**Availability**:
- iOS 17.5+
- iPadOS 17.5+
- Mac Catalyst 17.5+
- visionOS ?+

## Declaration

```swift
@discardableResult
mutating func merge(_ other: AssignableDocument) async throws -> Bool
```

#### Return Value

`true`, if the merge caused a mutation.

## Parameters

- `other`: The other object to merge into this one.


---

*[View on Apple Developer](https://developer.apple.com/documentation/assignables/assignabledocument/merge(_:))*