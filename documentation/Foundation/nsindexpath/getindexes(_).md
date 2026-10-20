# getIndexes(_:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Copies the objects contained in the index path into indexes.

**Availability**:
- iOS 2.0+ - Deprecated in 27.2
- iPadOS 2.0+ - Deprecated in 27.2
- Mac Catalyst 13.1+ - Deprecated in 27.2
- macOS 10.0+ - Deprecated in 27.2
- tvOS 9.0+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2
- watchOS 2.0+ - Deprecated in 27.2

> **Deprecated**: Use [`getIndexes(_:range:)`](./getindexes%28_,range%29.md) instead.

## Declaration

```swift
func getIndexes(_ indexes: UnsafeMutablePointer<Int>)
```

```objc
- (void) getIndexes:(NSUInteger *) indexes;
```

#### Discussion

You must allocate the memory for the C array.

## Parameters

- `indexes`: Pointer to a C array of objects of size at least the length of the index path. On return, the index path’s indexes.

## See Also

### Working with Indexes
- [func index(atPosition: Int) -> Int](./index%28atposition%29.md)
  Provides the value at a particular node in the index path.
- [func getIndexes(UnsafeMutablePointer<Int>, range: NSRange)](./getindexes%28_,range%29.md)
  Copies the indexes stored in the index path from the positions specified by the position range into the specified indexes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsindexpath/getindexes(_:))*