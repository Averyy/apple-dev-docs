# keyEnumerator()

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (NSEnumerator<id> *) keyEnumerator;
```

#### Return Value

An enumerator object that lets you access each key in the dictionary.

#### Discussion

Here’s how you might use this method.

**Swift**:

```swift
let enumerator = myDictionary.keyEnumerator()

while let key = enumerator.nextObject() {
    /* code that uses the returned key */
}

```

**Objective-C**:

```objc
NSEnumerator *enumerator = [myDictionary keyEnumerator];
id key;
 
while ((key = [enumerator nextObject])) {
    /* code that uses the returned key */
}
```

If you use this method with instances of mutable subclasses of [`NSDictionary`](../nsdictionary.md), your code should not modify the entries during enumeration. If you intend to modify the entries, use the [`allKeys`](./allkeys.md) property to create a snapshot of the dictionary’s keys. Then use this snapshot to traverse the entries, modifying them along the way.

If you want to enumerate the dictionary’s values rather than its keys, use the [`objectEnumerator()`](./objectenumerator%28%29.md) method.

##### Special Considerations

It is more efficient to use the fast enumeration protocol (see [`NSFastEnumeration`](../nsfastenumeration.md)) than this method. Fast enumeration is available in macOS 10.5 and later and iOS 2.0 and later.

## See Also

### Enumerating Dictionaries
- [func objectEnumerator() -> NSEnumerator](./objectenumerator%28%29.md)
  Returns an enumerator object that lets you access each value in the dictionary.
- [func enumerateKeysAndObjects((Any, Any, UnsafeMutablePointer<ObjCBool>) -> Void)](./enumeratekeysandobjects%28_%29.md)
  Applies a given block object to the entries of the dictionary.
- [func enumerateKeysAndObjects(options: NSEnumerationOptions, using: (Any, Any, UnsafeMutablePointer<ObjCBool>) -> Void)](./enumeratekeysandobjects%28options,using%29.md)
  Applies a given block object to the entries of the dictionary, with options specifying how the enumeration is performed.
- [func makeIterator() -> NSDictionary.Iterator](./makeiterator%28%29.md)
  Returns an iterator over the elements of this sequence.
- [- countByEnumeratingWithState:objects:count:](./countbyenumeratingwithstate_objects_count_.md)
  Returns by reference a C array of objects over which the sender should iterate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdictionary/keyenumerator())*