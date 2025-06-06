# setObjectValue(_:)

**Framework**: AppKit  
**Kind**: method

Sets the receiver’s object value.

**Availability**:
- macOS 10.5+

## Declaration

```swift
@MainActor
func setObjectValue(_ obj: (any NSCopying)?)
```

#### Discussion

If `setObjectValue:` is called with an `NSURL` object, [`clickedPathComponentCell`](nspathcell/clickedpathcomponentcell.md) is automatically called. The [`objectValue`](nscell/objectvalue.md) method returns the most recently set URL value. The `setObjectValue:` method can also take a string value, with the items separated by the path separator (`/`). Any other value is a programming error and will cause an assertion.

## Parameters

- `obj`: The new object value for the cell.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspathcell/setobjectvalue(_:))*