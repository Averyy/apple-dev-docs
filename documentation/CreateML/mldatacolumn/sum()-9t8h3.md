# sum()

**Framework**: Create ML  
**Kind**: method  
**Role**: Instance Method

Returns the sum of the elements in a column of integers.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.14+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
func sum() -> Int?
```

Available when `Element` is `Int`.

**Other overloads**:

```swift
func sum() -> Double?
```

## Return Value

An [`Int`](../../Swift/int.md); otherwise `nil` if the column is invalid.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mldatacolumn/sum()-9t8h3)*