# enumerateKeysAndObjects(options:using:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Applies a given block object to the entries of the dictionary, with options specifying how the enumeration is performed.

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
func enumerateKeysAndObjects(options opts: NSEnumerationOptions = [], using block: (Any, Any, UnsafeMutablePointer<ObjCBool>) -> Void)
```

```objc
- (void) enumerateKeysAndObjectsWithOptions:(NSEnumerationOptions) opts usingBlock:(void (^)(KeyType key, ObjectType obj, BOOL *stop)) block;
```

## Discussion

If the block sets `*stop` to [`true`](../../Swift/true.md), the enumeration stops.

## Parameters

- `opts`: Enumeration options.
- `block`: A block object to operate on entries in the dictionary.

## See Also

### Enumerating Dictionaries
- [func keyEnumerator() -> NSEnumerator](./keyenumerator%28%29.md)
  Provides an enumerator to access the keys in the dictionary.
- [func objectEnumerator() -> NSEnumerator](./objectenumerator%28%29.md)
  Returns an enumerator object that lets you access each value in the dictionary.
- [func enumerateKeysAndObjects((Any, Any, UnsafeMutablePointer<ObjCBool>) -> Void)](./enumeratekeysandobjects%28_%29.md)
  Applies a given block object to the entries of the dictionary.
- [func makeIterator() -> NSDictionary.Iterator](./makeiterator%28%29.md)
  Returns an iterator over the elements of this sequence.
- [- countByEnumeratingWithState:objects:count:](./countbyenumeratingwithstate_objects_count_.md)
  Returns by reference a C array of objects over which the sender should iterate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdictionary/enumeratekeysandobjects(options:using:))*