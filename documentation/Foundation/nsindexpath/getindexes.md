# getIndexes(_:)

**Framework**: Foundation  
**Kind**: method

Copies the objects contained in the index path into indexes.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func getIndexes(_ indexes: UnsafeMutablePointer<Int>)
```

#### Discussion

You must allocate the memory for the C array.

## Parameters

- `indexes`: Pointer to a C array of objects of size at least the length of the index path. On return, the index path’s indexes.

## See Also

- [func index(atPosition: Int) -> Int](nsindexpath/index(atposition:).md)
  Provides the value at a particular node in the index path.
- [func getIndexes(UnsafeMutablePointer<Int>, range: NSRange)](nsindexpath/getindexes(_:range:).md)
  Copies the indexes stored in the index path from the positions specified by the position range into the specified indexes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsindexpath/getindexes(_:))*