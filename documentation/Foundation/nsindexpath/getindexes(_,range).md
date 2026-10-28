# getIndexes(_:range:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Copies the indexes stored in the index path from the positions specified by the position range into the specified indexes.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func getIndexes(_ indexes: UnsafeMutablePointer<Int>, range positionRange: NSRange)
```

```objc
- (void) getIndexes:(NSUInteger *) indexes range:(NSRange) positionRange;
```

## Discussion

You must allocate the memory for the C array.

## Parameters

- `indexes`: Pointer to a C array of at least as many [`NSUInteger`](../../ObjectiveC/nsuinteger.md) objects as specified by the length of `positionRange`. On return, the array holds the index path’s indexes.
- `positionRange`: A range of valid positions within the index path. If the location plus the length of `positionRange` is greater than the length of the index path, this method raises an [`rangeException`](../nsexceptionname/rangeexception.md).

## See Also

### Working with Indexes
- [func index(atPosition: Int) -> Int](./index%28atposition%29.md)
  Provides the value at a particular node in the index path.
- [func getIndexes(UnsafeMutablePointer<Int>)](./getindexes%28_%29.md)
  Copies the objects contained in the index path into indexes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsindexpath/getindexes(_:range:))*