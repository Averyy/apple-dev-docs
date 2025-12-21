# setPath(_:)

**Framework**: AppKit  
**Kind**: method

Sets the path to be displayed by the browser.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func setPath(_ path: String) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if the given path is valid; otherwise, [`false`](https://developer.apple.com/documentation/Swift/false).

#### Discussion

While parsing `path`, the browser compares each component with the entries in the current column. If an exact match is found, the matching entry is selected, and the next component is compared to the next column’s entries. If no match is found for a component, the method exits and returns [`false`](https://developer.apple.com/documentation/Swift/false); the final path is set to the valid portion of `path`. If each component of `path` specifies a valid branch or leaf in the browser’s hierarchy, the method returns [`true`](https://developer.apple.com/documentation/Swift/true).

## Parameters

- `path`: The path to display. If   is prefixed by the path separator, the path is absolute, containing the full path from the browser’s first column. Otherwise, the path is relative, extending the browser’s current path starting at the last column.

## See Also

- [func path() -> String](nsbrowser/path.md)
  Returns a string representing the browser’s current path.
- [func path(toColumn: Int) -> String](nsbrowser/path(tocolumn:).md)
  Returns a string representing the path from the first column up to, but not including, the column at the given index.
- [var pathSeparator: String](nsbrowser/pathseparator.md)
  The path separator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbrowser/setpath(_:))*