# enumerateRanges(options:using:)

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
func enumerateRanges(options opts: NSEnumerationOptions = [], using block: (NSRange, UnsafeMutablePointer<ObjCBool>) -> Void)
```

#### Discussion

By default, the enumeration starts with the first object and continues serially through the indexed set range to the last object in the range. You can specify `NSEnumerationConcurrent` and/or `NSEnumerationReverse` as enumeration options to modify this behavior.

This method executes synchronously.

> ❗ **Important**:  If the Block parameter is `nil` this method will raise an exception.

## Parameters

- `opts`: A bitmask that specifies the   for the enumeration (whether it should be performed concurrently and whether it should be performed in reverse order).
- `block`: The block takes two arguments:

## See Also

- [func enumerateRanges(in: NSRange, options: NSEnumerationOptions, using: (NSRange, UnsafeMutablePointer<ObjCBool>) -> Void)](nsindexset/enumerateranges(in:options:using:).md)
  Enumerates over the ranges in the range of objects using the block
- [func enumerateRanges((NSRange, UnsafeMutablePointer<ObjCBool>) -> Void)](nsindexset/enumerateranges(_:).md)
  Executes a given block using each object in the index set, in the specified ranges.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsindexset/enumerateranges(options:using:))*