# enumerate(in:options:using:)

**Framework**: Foundation  
**Kind**: method

Executes a given Block using the indexes in the specified range, using the specified enumeration options.

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
func enumerate(in range: NSRange, options opts: NSEnumerationOptions = [], using block: (Int, UnsafeMutablePointer<ObjCBool>) -> Void)
```

#### Discussion

This method executes synchronously.

## Parameters

- `range`: The range to enumerate.
- `opts`: A bitmask that specifies the options for the enumeration (whether it should be performed concurrently and whether it should be performed in reverse order). See   for the supported values.
- `block`: The Block takes two arguments:

## See Also

- [func enumerate((Int, UnsafeMutablePointer<ObjCBool>) -> Void)](nsindexset/enumerate(_:).md)
  Executes a given Block using each object in the index set.
- [func enumerate(options: NSEnumerationOptions, using: (Int, UnsafeMutablePointer<ObjCBool>) -> Void)](nsindexset/enumerate(options:using:).md)
  Executes a given Block over the index set’s indexes, using the specified enumeration options.
- [func makeIterator() -> NSIndexSetIterator](nsindexset/makeiterator.md)
  Returns an  over the elements of this .
- [struct NSIndexSetIterator](nsindexsetiterator.md)
  An iterator suitable for enumerating the elements of an index set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsindexset/enumerate(in:options:using:))*