# std()

**Framework**: Create ML  
**Kind**: method  
**Role**: Instance Method

Returns the standard deviation of the elements in a column of integers.

**Availability**:
- iOS 15.0+ - Deprecated in 16.0 (renamed: stdev)
- iPadOS 15.0+ - Deprecated in 16.0 (renamed: stdev)
- Mac Catalyst 15.0+ - Deprecated in 16.0 (renamed: stdev)
- macOS 10.14+ - Deprecated in 10.15 (renamed: stdev)
- visionOS 1.0+

## Declaration

```swift
func std() -> Double?
```

Available when `Element` is `Int`.

**Other overloads**:

```swift
func std() -> Double?
```

## Return Value

A [`Double`](../../Swift/double.md); otherwise `nil` if the column is invalid.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mldatacolumn/std()-69udj)*