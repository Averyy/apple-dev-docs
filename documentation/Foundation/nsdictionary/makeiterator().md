# makeIterator()

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Returns an iterator over the elements of this sequence.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func makeIterator() -> NSDictionary.Iterator
```

#### Discussion

Complexity: O(1).

## See Also

### Enumerating Dictionaries
- [func keyEnumerator() -> NSEnumerator](./keyenumerator%28%29.md)
  Provides an enumerator to access the keys in the dictionary.
- [func objectEnumerator() -> NSEnumerator](./objectenumerator%28%29.md)
  Returns an enumerator object that lets you access each value in the dictionary.
- [func enumerateKeysAndObjects((Any, Any, UnsafeMutablePointer<ObjCBool>) -> Void)](./enumeratekeysandobjects%28_%29.md)
  Applies a given block object to the entries of the dictionary.
- [func enumerateKeysAndObjects(options: NSEnumerationOptions, using: (Any, Any, UnsafeMutablePointer<ObjCBool>) -> Void)](./enumeratekeysandobjects%28options,using%29.md)
  Applies a given block object to the entries of the dictionary, with options specifying how the enumeration is performed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdictionary/makeiterator())*