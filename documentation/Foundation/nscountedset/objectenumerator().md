# objectEnumerator()

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Returns an enumerator object that lets you access each object in the set once, independent of its count.

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
func objectEnumerator() -> NSEnumerator
```

```objc
- (NSEnumerator<id> *) objectEnumerator;
```

#### Return Value

An enumerator object that lets you access each object in the set once, independent of its count.

#### Discussion

If you add a given object to the counted set multiple times, an enumeration of the set will produce that object only once.

You shouldn’t modify the set during enumeration. If you intend to modify the set, use the [`allObjects`](../nsset/allobjects.md) method to create a “snapshot,” then enumerate the snapshot and modify the original set.

## See Also

### Related Documentation
- [func nextObject() -> Any?](../nsenumerator/nextobject%28%29.md)
  Returns the next object from the collection being enumerated.
### Examining a Counted Set
- [func count(for: Any) -> Int](./count%28for%29.md)
  Returns the count associated with a given object in the set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nscountedset/objectenumerator())*