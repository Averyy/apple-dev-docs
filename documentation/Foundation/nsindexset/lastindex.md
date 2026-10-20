# lastIndex

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

The last index in the index set.

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
var lastIndex: Int { get }
```

```objc
@property (readonly) NSUInteger lastIndex;
```

#### Discussion

Last index in the index set or NSNotFound when the index set is empty.

## See Also

### Getting Indexes
- [var firstIndex: Int](./firstindex.md)
  The first index in the index set.
- [func indexLessThanIndex(Int) -> Int](./indexlessthanindex%28_%29.md)
  Returns either the closest index in the index set that is less than a specific index or the not-found indicator.
- [func indexLessThanOrEqual(to: Int) -> Int](./indexlessthanorequal%28to%29.md)
  Returns either the closest index in the index set that is less than or equal to a specific index or the not-found indicator.
- [func indexGreaterThanOrEqual(to: Int) -> Int](./indexgreaterthanorequal%28to%29.md)
  Returns either the closest index in the index set that is greater than or equal to a specific index or the not-found indicator.
- [func indexGreaterThanIndex(Int) -> Int](./indexgreaterthanindex%28_%29.md)
  Returns either the closest index in the index set that is greater than a specific index or the not-found indicator.
- [func getIndexes(UnsafeMutablePointer<Int>, maxCount: Int, inIndexRange: NSRangePointer?) -> Int](./getindexes%28_,maxcount,inindexrange%29.md)
  The index set fills an index buffer with the indexes contained both in the index set and in an index range, returning the number of indexes copied.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsindexset/lastindex)*