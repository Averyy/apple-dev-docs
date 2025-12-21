# isValid

**Framework**: Create ML  
**Kind**: property

A Boolean value that indicates whether the column is valid.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.14+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
var isValid: Bool { get }
```

#### Discussion

Check [`isValid`](mluntypedcolumn/isvalid.md) after you create or mutate an untyped column to ensure it’s valid. If the value is [`false`](https://developer.apple.com/documentation/Swift/false), the untyped column encountered an error and you can’t use it for subsequent operations. For example, comparing two columns of different sizes creates an invalid column.

## See Also

- [var error: (any Error)?](mluntypedcolumn/error.md)
  The underlying error present when the column is invalid.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mluntypedcolumn/isvalid)*