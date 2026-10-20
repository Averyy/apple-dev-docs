# subscript(_:)

**Framework**: SwiftUI  
**Kind**: subscript  
**Role**: Instance Subscript

Gets the subview proxies in the specified range.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
subscript(bounds: Range<Int>) -> LayoutSubviews { get }
```

**Other overloads**:

```swift
subscript(index: Int) -> LayoutSubviews.Element { get }
```

```swift
subscript<S>(indices: S) -> LayoutSubviews where S : Sequence, S.Element == Int { get }
```

## See Also

### Accessing subviews
- [var startIndex: Int](./startindex.md)
  The index of the first subview.
- [var endIndex: Int](./endindex.md)
  An index that’s one higher than the last subview.
- [LayoutSubviews.Element](./element.md)
  A type that contains a proxy value.
- [LayoutSubviews.Index](./index.md)
  A type that you can use to index proxy values.
- [LayoutSubviews.SubSequence](./subsequence.md)
  A type that contains a subsequence of proxy values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/layoutsubviews/subscript(_:))*