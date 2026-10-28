# index(atPosition:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Provides the value at a particular node in the index path.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func index(atPosition position: Int) -> Int
```

```objc
- (NSUInteger) indexAtPosition:(NSUInteger) position;
```

## Return Value

The index value at `node` or `NSNotFound` if the node is outside the range of the index path.

## Parameters

- `position`: Index value of the desired node. Node numbering starts at zero.

## See Also

### Working with Indexes
- [func getIndexes(UnsafeMutablePointer<Int>, range: NSRange)](./getindexes%28_,range%29.md)
  Copies the indexes stored in the index path from the positions specified by the position range into the specified indexes.
- [func getIndexes(UnsafeMutablePointer<Int>)](./getindexes%28_%29.md)
  Copies the objects contained in the index path into indexes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsindexpath/index(atposition:))*