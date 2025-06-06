# ReferenceComponent.LoadingPolicy

**Framework**: RealityKit  
**Kind**: enum

Describes when a referenced entity loads.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
enum LoadingPolicy
```

## Topics

### Operators
- [static func == (ReferenceComponent.LoadingPolicy, ReferenceComponent.LoadingPolicy) -> Bool](referencecomponent/loadingpolicy-swift.enum/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Enumeration Cases
- [ReferenceComponent.LoadingPolicy.immediate](referencecomponent/loadingpolicy-swift.enum/immediate.md)
  Loads the contents from the referenced entity file immediately when the root entity loads.
- [ReferenceComponent.LoadingPolicy.onDemand](referencecomponent/loadingpolicy-swift.enum/ondemand.md)
  Loads the contents from the referenced entity file when your app tells it to.
### Instance Properties
- [var hashValue: Int](referencecomponent/loadingpolicy-swift.enum/hashvalue.md)
  The hash value.
### Instance Methods
- [func hash(into: inout Hasher)](referencecomponent/loadingpolicy-swift.enum/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Default Implementations
- [Equatable Implementations](referencecomponent/loadingpolicy-swift.enum/equatable-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/referencecomponent/loadingpolicy-swift.enum)*