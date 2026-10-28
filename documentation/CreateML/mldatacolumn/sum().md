# sum()

**Framework**: Create ML  
**Kind**: method  
**Role**: Instance Method

Returns the sum of the elements in a column of doubles.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.14+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
func sum() -> Double?
```

Available when `Element` is `Double`.

**Other overloads**:

```swift
func sum() -> Int?
```

## Return Value

A [`Double`](../../Swift/double.md); otherwise `nil` if the column is invalid.

## See Also

### Getting sum, mean, and standard deviation values
- [func mean()](./mean%28%29.md)
  Returns the arithmetic mean of the elements in a column of doubles.
- [func std()](./std%28%29.md)
  Returns the standard deviation of the elements in a column of doubles.
- [func stdev()](./stdev%28%29.md)
  Returns the standard deviation of the elements in a column of doubles.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mldatacolumn/sum())*