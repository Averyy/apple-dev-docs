# max()

**Framework**: Create ML  
**Kind**: method  
**Role**: Instance Method

Returns the element with the highest value in a column of doubles.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.14+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
func max() -> Double?
```

Available when `Element` is `Double`.

**Other overloads**:

```swift
func max() -> Int?
```

## Return Value

A [`Double`](../../Swift/double.md); otherwise `nil` if the column is empty or invalid.

## See Also

### Getting the min and max element values
- [func min()](./min%28%29.md)
  Returns the element with the lowest value in a column of doubles.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mldatacolumn/max())*