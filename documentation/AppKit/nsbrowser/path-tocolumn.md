# path(toColumn:)

**Framework**: AppKit  
**Kind**: method

Returns a string representing the path from the first column up to, but not including, the column at the given index.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func path(toColumn column: Int) -> String
```

#### Return Value

The path of the current selection up to, but not including, the specified column. The components of this path are separated with the string returned by [`pathSeparator`](nsbrowser/pathseparator.md).

## Parameters

- `column`: The index of the column at which the path stops.

## See Also

- [func path() -> String](nsbrowser/path.md)
  Returns a string representing the browser’s current path.
- [func setPath(String) -> Bool](nsbrowser/setpath(_:).md)
  Sets the path to be displayed by the browser.
- [var pathSeparator: String](nsbrowser/pathseparator.md)
  The path separator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbrowser/path(tocolumn:))*