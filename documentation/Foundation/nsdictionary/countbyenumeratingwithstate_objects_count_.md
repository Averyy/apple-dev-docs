# countByEnumeratingWithState:objects:count:

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Returns by reference a C array of objects over which the sender should iterate.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```objc
- (NSUInteger) countByEnumeratingWithState:(NSFastEnumerationState *) state objects:(K[]) buffer count:(NSUInteger) len;
```

## Return Value

The number of objects returned in `buffer`. Returns `0` when the iteration is finished.

## Parameters

- `state`: Context information that is used in the enumeration to, in addition to other possibilities, ensure that the collection has not been mutated.
- `buffer`: A C array of objects over which the sender is to iterate.
- `len`: The maximum number of objects to return in `buffer`.

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

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdictionary/countbyenumeratingwithstate:objects:count:)*