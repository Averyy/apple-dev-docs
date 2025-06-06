# objectEnumerator()

**Framework**: Foundation  
**Kind**: method

Returns an enumerator object that lets you access each value in the map table.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func objectEnumerator() -> NSEnumerator?
```

#### Return Value

An enumerator object that lets you access each value in the map table.

#### Discussion

The following code fragment illustrates how you might use the method.

```objc
NSEnumerator *enumerator = [myMapTable objectEnumerator];
id value;
 
while ((value = [enumerator nextObject])) {
    /* code that acts on the map table's values */
}
```

##### Special Considerations

It is more efficient to use the fast enumeration protocol (see [`NSFastEnumeration`](nsfastenumeration.md)).

## See Also

- [func object(forKey: KeyType?) -> ObjectType?](nsmaptable/object(forkey:).md)
  Returns a the value associated with a given key.
- [func keyEnumerator() -> NSEnumerator](nsmaptable/keyenumerator.md)
  Returns an enumerator object that lets you access each key in the map table.
- [var count: Int](nsmaptable/count.md)
  The number of key-value pairs in the map table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmaptable/objectenumerator())*