# view(atColumn:)

**Framework**: AppKit  
**Kind**: method

Provides access to the given view at a particular column.

**Availability**:
- macOS 10.7+

## Declaration

```swift
@MainActor
func view(atColumn column: Int) -> Any?
```

#### Return Value

The view for the specified column.

#### Discussion

This is the only way to access cell views after the row view has been removed from the table.

## Parameters

- `column`: The index of the column.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstablerowview/view(atcolumn:))*