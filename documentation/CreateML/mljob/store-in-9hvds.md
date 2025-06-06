# store(in:)

**Framework**: Create ML  
**Kind**: method

Stores this cancellable instance in the specified collection.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
func store<C>(in collection: inout C) where C : RangeReplaceableCollection, C.Element == AnyCancellable
```

## Parameters

- `collection`: The collection in which to store this  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mljob/store(in:)-9hvds)*