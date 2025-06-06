# ReferenceComponent.ReferenceState

**Framework**: RealityKit  
**Kind**: enum

Defines the current loading state of the referenced entity.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
enum ReferenceState
```

## Topics

### Operators
- [static func == (ReferenceComponent.ReferenceState, ReferenceComponent.ReferenceState) -> Bool](referencecomponent/referencestate/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Enumeration Cases
- [ReferenceComponent.ReferenceState.loaded](referencecomponent/referencestate/loaded.md)
  The reference is loaded.
- [ReferenceComponent.ReferenceState.loading](referencecomponent/referencestate/loading.md)
  The reference is loading.
- [ReferenceComponent.ReferenceState.notLoaded](referencecomponent/referencestate/notloaded.md)
  The reference isn’t loaded.
### Instance Properties
- [var hashValue: Int](referencecomponent/referencestate/hashvalue.md)
  The hash value.
### Instance Methods
- [func hash(into: inout Hasher)](referencecomponent/referencestate/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Default Implementations
- [Equatable Implementations](referencecomponent/referencestate/equatable-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/referencecomponent/referencestate)*