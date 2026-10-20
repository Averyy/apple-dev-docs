# makeIterator()

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Returns an *iterator* over the elements of this *sequence*.

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
func makeIterator() -> NSIndexSetIterator
```

#### Discussion

Complexity: O(1).

## See Also

### Enumerating Indexes
- [func enumerate((Int, UnsafeMutablePointer<ObjCBool>) -> Void)](./enumerate%28_%29.md)
  Executes a given Block using each object in the index set.
- [func enumerate(options: NSEnumerationOptions, using: (Int, UnsafeMutablePointer<ObjCBool>) -> Void)](./enumerate%28options,using%29.md)
  Executes a given Block over the index set’s indexes, using the specified enumeration options.
- [func enumerate(in: NSRange, options: NSEnumerationOptions, using: (Int, UnsafeMutablePointer<ObjCBool>) -> Void)](./enumerate%28in,options,using%29.md)
  Executes a given Block using the indexes in the specified range, using the specified enumeration options.
- [struct NSIndexSetIterator](../nsindexsetiterator.md)
  An iterator suitable for enumerating the elements of an index set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsindexset/makeiterator())*