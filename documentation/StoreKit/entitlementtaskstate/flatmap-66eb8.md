# flatMap(_:)

**Framework**: StoreKit  
**Kind**: method

Returns a new state, mapping the entitlement value if successful.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
func flatMap<NewValue>(_ transform: (Value) async throws -> EntitlementTaskState<NewValue>) async rethrows -> EntitlementTaskState<NewValue>
```

## See Also

- [func flatMap<NewValue>((Value) throws -> EntitlementTaskState<NewValue>) rethrows -> EntitlementTaskState<NewValue>](entitlementtaskstate/flatmap(_:)-7gsnv.md)
  Returns a new state, mapping the entitlement value if successful.
- [func map<NewValue>((Value) throws -> NewValue) rethrows -> EntitlementTaskState<NewValue>](entitlementtaskstate/map(_:)-8ly3v.md)
  Returns a new state, mapping the entitlement value if successful.
- [func map<NewValue>((Value) async throws -> NewValue) async rethrows -> EntitlementTaskState<NewValue>](entitlementtaskstate/map(_:)-250dk.md)
  Returns a new state, mapping the entitlement value if successful.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/entitlementtaskstate/flatmap(_:)-66eb8)*