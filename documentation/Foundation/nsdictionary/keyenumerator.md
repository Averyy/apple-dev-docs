# keyEnumerator()

**Framework**: Foundation  
**Kind**: method

Provides an enumerator to access the keys in the dictionary.

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
func keyEnumerator() -> NSEnumerator
```

#### Return Value

An enumerator object that lets you access each key in the dictionary.

#### Discussion

Here’s how you might use this method.

If you use this method with instances of mutable subclasses of [`NSDictionary`](nsdictionary.md), your code should not modify the entries during enumeration. If you intend to modify the entries, use the [`allKeys`](nsdictionary/allkeys.md) property to create a snapshot of the dictionary’s keys. Then use this snapshot to traverse the entries, modifying them along the way.

If you want to enumerate the dictionary’s values rather than its keys, use the [`objectEnumerator()`](nsdictionary/objectenumerator().md) method.

##### Special Considerations

It is more efficient to use the fast enumeration protocol (see [`NSFastEnumeration`](nsfastenumeration.md)) than this method. Fast enumeration is available in macOS 10.5 and later and iOS 2.0 and later.

## See Also

- [func objectEnumerator() -> NSEnumerator](nsdictionary/objectenumerator.md)
  Returns an enumerator object that lets you access each value in the dictionary.
- [func enumerateKeysAndObjects((Any, Any, UnsafeMutablePointer<ObjCBool>) -> Void)](nsdictionary/enumeratekeysandobjects(_:).md)
  Applies a given block object to the entries of the dictionary.
- [func enumerateKeysAndObjects(options: NSEnumerationOptions, using: (Any, Any, UnsafeMutablePointer<ObjCBool>) -> Void)](nsdictionary/enumeratekeysandobjects(options:using:).md)
  Applies a given block object to the entries of the dictionary, with options specifying how the enumeration is performed.
- [func makeIterator() -> NSDictionary.Iterator](nsdictionary/makeiterator.md)
  Returns an iterator over the elements of this sequence.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdictionary/keyenumerator())*