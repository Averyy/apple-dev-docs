# enumerateKeysAndObjects(_:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Applies a given block object to the entries of the dictionary.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.6+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func enumerateKeysAndObjects(_ block: (Any, Any, UnsafeMutablePointer<ObjCBool>) -> Void)
```

```objc
- (void) enumerateKeysAndObjectsUsingBlock:(void (^)(KeyType key, ObjectType obj, BOOL *stop)) block;
```

#### Discussion

If the block sets `*stop` to [`true`](../../Swift/true.md), the enumeration stops.

## Parameters

- `block`: A block object to operate on entries in the dictionary.

## See Also

### Enumerating Dictionaries
- [func keyEnumerator() -> NSEnumerator](./keyenumerator%28%29.md)
  Provides an enumerator to access the keys in the dictionary.
- [func objectEnumerator() -> NSEnumerator](./objectenumerator%28%29.md)
  Returns an enumerator object that lets you access each value in the dictionary.
- [func enumerateKeysAndObjects(options: NSEnumerationOptions, using: (Any, Any, UnsafeMutablePointer<ObjCBool>) -> Void)](./enumeratekeysandobjects%28options,using%29.md)
  Applies a given block object to the entries of the dictionary, with options specifying how the enumeration is performed.
- [func makeIterator() -> NSDictionary.Iterator](./makeiterator%28%29.md)
  Returns an iterator over the elements of this sequence.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdictionary/enumeratekeysandobjects(_:))*