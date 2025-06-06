# subscript(_:)

**Framework**: Foundation  
**Kind**: subscript

Returns the object at the specified index of the set.

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
subscript(idx: Int) -> Any { get set }
```

#### Return Value

If `index` is beyond the end of the ordered set (that is, if index is greater than or equal to the value returned by count), an [`rangeException`](nsexceptionname/rangeexception.md) is raised.

#### Discussion

This method is the same as [`object(at:)`](nsorderedset/object(at:).md).

## Parameters

- `idx`: The object located at index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmutableorderedset/subscript(_:))*