# objectEnumerator()

**Framework**: Foundation  
**Kind**: method

Returns an enumerator object that lets you access each value in the dictionary.

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

#### Return Value

An enumerator object that lets you access each value in the dictionary.

#### Discussion

The following code fragment illustrates how you might use the method.

```objc
NSEnumerator *enumerator = [myDictionary objectEnumerator];
id value;
 
while ((value = [enumerator nextObject])) {
    /* code that acts on the dictionary’s values */
}
```

If you use this method with instances of mutable subclasses of `NSDictionary`, your code should not modify the entries during enumeration. If you intend to modify the entries, use the [`allValues`](nsdictionary/allvalues.md) method to create a “snapshot” of the dictionary’s values. Work from this snapshot to modify the values.

##### Special Considerations

It is more efficient to use the fast enumeration protocol (see [`NSFastEnumeration`](nsfastenumeration.md)). Fast enumeration is available in macOS 10.5 and later and iOS 2.0 and later.

## See Also

- [func nextObject() -> Any?](nsenumerator/nextobject.md)
  Returns the next object from the collection being enumerated.
- [func keyEnumerator() -> NSEnumerator](nsdictionary/keyenumerator.md)
  Provides an enumerator to access the keys in the dictionary.
- [func enumerateKeysAndObjects((Any, Any, UnsafeMutablePointer<ObjCBool>) -> Void)](nsdictionary/enumeratekeysandobjects(_:).md)
  Applies a given block object to the entries of the dictionary.
- [func enumerateKeysAndObjects(options: NSEnumerationOptions, using: (Any, Any, UnsafeMutablePointer<ObjCBool>) -> Void)](nsdictionary/enumeratekeysandobjects(options:using:).md)
  Applies a given block object to the entries of the dictionary, with options specifying how the enumeration is performed.
- [func makeIterator() -> NSDictionary.Iterator](nsdictionary/makeiterator.md)
  Returns an iterator over the elements of this sequence.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdictionary/objectenumerator())*