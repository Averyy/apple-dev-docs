# next(isolation:)

**Framework**: ManagedAppDistribution  
**Kind**: method

Asynchronously advances to the next element and returns it, or ends the sequence if there is no next element.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- visionOS 2.4+

## Declaration

```swift
func next(isolation actor: isolated (any Actor)?) async throws(ManagedAppLibrary.ManagedApps.AsyncIterator.Failure) -> ManagedAppLibrary.ManagedApps.AsyncIterator.Element?
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/managedappdistribution/managedapplibrary/managedapps/asynciterator/next(isolation:))*