# enumerateRanges(_:)

**Framework**: Foundation  
**Kind**: method

Executes a given block using each object in the index set, in the specified ranges.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func enumerateRanges(_ block: (NSRange, UnsafeMutablePointer<ObjCBool>) -> Void)
```

#### Discussion

If the Block parameter is `nil` this method will raise an exception.

This method executes synchronously.

## Parameters

- `block`: The block takes two arguments:

## See Also

- [func enumerateRanges(in: NSRange, options: NSEnumerationOptions, using: (NSRange, UnsafeMutablePointer<ObjCBool>) -> Void)](nsindexset/enumerateranges(in:options:using:).md)
  Enumerates over the ranges in the range of objects using the block
- [func enumerateRanges(options: NSEnumerationOptions, using: (NSRange, UnsafeMutablePointer<ObjCBool>) -> Void)](nsindexset/enumerateranges(options:using:).md)
  Executes a given block using each object in the index set, in the specified ranges.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsindexset/enumerateranges(_:))*