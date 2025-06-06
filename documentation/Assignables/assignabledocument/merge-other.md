# merge(other:)

**Framework**: Assignables  
**Kind**: method

Merge another object of this type into this object.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+
- Unknown ?+ - Deprecated
- visionOS ?+

## Declaration

```swift
@discardableResult
mutating func merge(other: AssignableDocument) throws -> Bool
```

#### Discussion

An exception is thrown if `other` is not a replica of this document.

## Parameters

- `other`: The other object to merge into this one.


---

*[View on Apple Developer](https://developer.apple.com/documentation/assignables/assignabledocument/merge(other:))*