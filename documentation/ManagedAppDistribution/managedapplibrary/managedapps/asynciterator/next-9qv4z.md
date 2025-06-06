# next()

**Framework**: ManagedAppDistribution  
**Kind**: method

Default implementation of `next()` in terms of `next(isolation:)`, which is required to maintain backward compatibility with existing async iterators.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
mutating func next() async throws(Self.Failure) -> Self.Element?
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/managedappdistribution/managedapplibrary/managedapps/asynciterator/next()-9qv4z)*