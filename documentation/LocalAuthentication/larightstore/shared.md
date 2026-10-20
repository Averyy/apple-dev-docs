# shared

**Framework**: Local Authentication  
**Kind**: property  
**Role**: Type Property

A shared object that stores rights.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
class var shared: LARightStore { get }
```

```objc
@property (class, readonly) LARightStore * sharedStore;
```

## See Also

### Accessing rights
- [func right(forIdentifier: String, completion: (LAPersistedRight?, (any Error)?) -> Void)](./right%28foridentifier,completion%29.md)
  Fetches a previously stored right from the shared right store.


---

*[View on Apple Developer](https://developer.apple.com/documentation/localauthentication/larightstore/shared)*