# enumerateKeysAndObjects(options:using:)

**Framework**: Foundation  
**Kind**: method

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

#### Discussion

If the block sets `*stop` to [`true`](https://developer.apple.com/documentation/swift/true), the enumeration stops.

## Parameters

- `opts`: Enumeration options.
- `block`: A block object to operate on entries in the dictionary.

## See Also

- [func keyEnumerator() -> NSEnumerator](nsdictionary/keyenumerator.md)
  Provides an enumerator to access the keys in the dictionary.
- [func objectEnumerator() -> NSEnumerator](nsdictionary/objectenumerator.md)
  Returns an enumerator object that lets you access each value in the dictionary.
- [func enumerateKeysAndObjects((Any, Any, UnsafeMutablePointer<ObjCBool>) -> Void)](nsdictionary/enumeratekeysandobjects(_:).md)
  Applies a given block object to the entries of the dictionary.
- [func makeIterator() -> NSDictionary.Iterator](nsdictionary/makeiterator.md)
  Returns an iterator over the elements of this sequence.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdictionary/enumeratekeysandobjects(options:using:))*