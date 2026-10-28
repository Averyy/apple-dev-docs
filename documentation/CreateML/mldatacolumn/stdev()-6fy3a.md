# stdev()

**Framework**: Create ML  
**Kind**: method  
**Role**: Instance Method

Standard deviation of the Elements in the MLDataColumn.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.15+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
func stdev() -> Double?
```

Available when `Element` is `Int`.

**Other overloads**:

```swift
func stdev() -> Double?
```

## Return Value

Standard deviation of the Element values in the MLDataColumn. Returns nil if the MLDataColumn is invalid, 0 if the MLDataColumn is empty.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mldatacolumn/stdev()-6fy3a)*