# enumerateRanges(_:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (void) enumerateRangesUsingBlock:(void (^)(NSRange range, BOOL *stop)) block;
```

#### Discussion

If the Block parameter is `nil` this method will raise an exception.

This method executes synchronously.

## Parameters

- `block`: The block to apply to elements in the index set.

  The block takes two arguments:

  - **range**: The range of objects of the elements in the index set.
  - **stop**: A reference to a Boolean value. The block can set the value to [`true`](../../Swift/true.md) to stop further processing of the array. The stop argument is an out-only argument. You should only ever set this Boolean to [`true`](../../Swift/true.md) within the Block.

## See Also

### Enumerating Index Set Content
- [func enumerateRanges(in: NSRange, options: NSEnumerationOptions, using: (NSRange, UnsafeMutablePointer<ObjCBool>) -> Void)](./enumerateranges%28in,options,using%29.md)
  Enumerates over the ranges in the range of objects using the block
- [func enumerateRanges(options: NSEnumerationOptions, using: (NSRange, UnsafeMutablePointer<ObjCBool>) -> Void)](./enumerateranges%28options,using%29.md)
  Executes a given block using each object in the index set, in the specified ranges.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsindexset/enumerateranges(_:))*