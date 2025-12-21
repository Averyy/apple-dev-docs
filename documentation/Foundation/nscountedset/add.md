# add(_:)

**Framework**: Foundation  
**Kind**: method

Adds a given object to the set.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func add(_ object: Any)
```

#### Discussion

If `object` is already a member, [`add(_:)`](nscountedset/add(_:).md) increments the count associated with the object. If `object` is not already a member, it is sent a [`retain`](https://developer.apple.com/documentation/ObjectiveC/NSObject-c.protocol/retain) message.

## Parameters

- `object`: The object to add to the set.

## See Also

- [func remove(Any)](nscountedset/remove(_:).md)
  Removes a given object from the set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nscountedset/add(_:))*