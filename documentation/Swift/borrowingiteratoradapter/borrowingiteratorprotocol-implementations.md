# BorrowingIteratorProtocol Implementations

**Framework**: Swift  
**Role**: API Collection

## Topics

### Instance Methods
- [func nextSpan() throws(Self.Failure) -> Span<Self.Element>](./nextspan%28%29.md)
  Returns a span over the next group of elements that are ready to by visited, up to the specifed maximum.
- [func skip(by: Int) throws(Self.Failure) -> Int](./skip%28by%29.md)
  Advances the position of this iterator by the specified offset, or until the end of the underlying type’s elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/borrowingiteratoradapter/borrowingiteratorprotocol-implementations)*