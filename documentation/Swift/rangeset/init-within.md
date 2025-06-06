# init(_:within:)

**Framework**: Swift  
**Kind**: init

Creates a new range set containing ranges that contain only the specified indices in the given collection.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
init<S, C>(_ indices: S, within collection: C) where Bound == S.Element, S : Sequence, C : Collection, S.Element == C.Index
```

## Parameters

- `collection`: The collection that contains  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/rangeset/init(_:within:))*