# add(_:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (void) addObject:(ObjectType) object;
```

#### Discussion

If `object` is already a member, [`add(_:)`](./add%28_%29.md) increments the count associated with the object. If `object` is not already a member, it is sent a [`retain`](../../ObjectiveC/nsobject-c.protocol/retain.md) message.

## Parameters

- `object`: The object to add to the set.

## See Also

### Adding and Removing Entries
- [func remove(Any)](./remove%28_%29.md)
  Removes a given object from the set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nscountedset/add(_:))*