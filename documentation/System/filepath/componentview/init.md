# init(_:)

**Framework**: System  
**Kind**: init

Creates a new instance of a collection containing the elements of a sequence.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
init<S>(_ elements: S) where S : Sequence, Self.Element == S.Element
```

## Parameters

- `elements`: The sequence of elements for the new collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/system/filepath/componentview/init(_:))*