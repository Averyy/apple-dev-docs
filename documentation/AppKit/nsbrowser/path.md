# path()

**Framework**: AppKit  
**Kind**: method

Returns a string representing the browser’s current path.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func path() -> String
```

#### Return Value

The path representing the current selection. The components of this path are separated with the string returned by [`pathSeparator`](nsbrowser/pathseparator.md).

#### Discussion

Invoking this method is equivalent to invoking [`path(toColumn:)`](nsbrowser/path(tocolumn:).md) for all columns.

## See Also

- [func setPath(String) -> Bool](nsbrowser/setpath(_:).md)
  Sets the path to be displayed by the browser.
- [func path(toColumn: Int) -> String](nsbrowser/path(tocolumn:).md)
  Returns a string representing the path from the first column up to, but not including, the column at the given index.
- [var pathSeparator: String](nsbrowser/pathseparator.md)
  The path separator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbrowser/path())*