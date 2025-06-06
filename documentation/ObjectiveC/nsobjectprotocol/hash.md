# hash

**Framework**: Objective-C Runtime  
**Kind**: property  
**Required**: Yes

Returns an integer that can be used as a table address in a hash table structure.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
var hash: Int { get }
```

#### Return Value

An integer that can be used as a table address in a hash table structure.

#### Discussion

If two objects are equal (as determined by the [`isEqual(_:)`](nsobjectprotocol/isequal(_:).md) method), they must have the same hash value. This last point is particularly important if you define [`hash`](nsobjectprotocol/hash.md) in a subclass and intend to put instances of that subclass into a collection.

If a mutable object is added to a collection that uses hash values to determine the object’s position in the collection, the value returned by the [`hash`](nsobjectprotocol/hash.md) method of the object must not change while the object is in the collection. Therefore, either the [`hash`](nsobjectprotocol/hash.md) method must not rely on any of the object’s internal state information or you must make sure the object’s internal state information does not change while the object is in the collection. Thus, for example, a mutable dictionary can be put in a hash table but you must not change it while it is in there. (Note that it can be difficult to know whether or not a given object is in a collection.)

## See Also

- [func isEqual(Any?) -> Bool](nsobjectprotocol/isequal(_:).md)
  Returns a Boolean value that indicates whether the receiver and a given object are equal.
- [func `self`() -> Self](nsobjectprotocol/self.md)
  Returns the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobjectprotocol/hash)*