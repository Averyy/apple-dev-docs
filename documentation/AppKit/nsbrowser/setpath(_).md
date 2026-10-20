# setPath(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Sets the path to be displayed by the browser.

**Availability**:
- macOS

## Declaration

```swift
func setPath(_ path: String) -> Bool
```

```objc
- (BOOL) setPath:(NSString *) path;
```

#### Return Value

[`true`](../../Swift/true.md) if the given path is valid; otherwise, [`false`](../../Swift/false.md).

#### Discussion

While parsing `path`, the browser compares each component with the entries in the current column. If an exact match is found, the matching entry is selected, and the next component is compared to the next column’s entries. If no match is found for a component, the method exits and returns [`false`](../../Swift/false.md); the final path is set to the valid portion of `path`. If each component of `path` specifies a valid branch or leaf in the browser’s hierarchy, the method returns [`true`](../../Swift/true.md).

## Parameters

- `path`: The path to display. If `path` is prefixed by the path separator, the path is absolute, containing the full path from the browser’s first column. Otherwise, the path is relative, extending the browser’s current path starting at the last column.

## See Also

### Managing the Path
- [func path() -> String](./path%28%29.md)
  Returns a string representing the browser’s current path.
- [func path(toColumn: Int) -> String](./path%28tocolumn%29.md)
  Returns a string representing the path from the first column up to, but not including, the column at the given index.
- [var pathSeparator: String](./pathseparator.md)
  The path separator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbrowser/setpath(_:))*