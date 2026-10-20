# argmax()

**Framework**: TabularData  
**Kind**: method  
**Role**: Instance Method

Returns the index of the element with the highest value.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
func argmax() -> FilledColumn<Base>.Index?
```

Available when `Base` conforms to `OptionalColumnProtocol` and `Base.WrappedElement` conforms to `Comparable`.

## See Also

### Finding an Element Index
- [func argmin() -> Base.Index?](./argmin%28%29.md)
  Returns the index of the element with the lowest value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/filledcolumn/argmax())*