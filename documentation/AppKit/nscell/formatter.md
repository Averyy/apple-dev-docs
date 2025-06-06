# formatter

**Framework**: AppKit  
**Kind**: property

The cell’s formatter object.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var formatter: Formatter? { get set }
```

#### Discussion

A formatter handles the translation of the receiver’s contents between its onscreen representation and its object value. Cells use a formatter object to format the textual representation of their object value and to validate cell input and convert that input to an object value. When assigning a new formatter to a cell, the formatter attempts to interpret the cell’s current value. If it cannot do so, the formatter converts the current value to a string object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscell/formatter)*