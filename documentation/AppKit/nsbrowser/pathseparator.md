# pathSeparator

**Framework**: AppKit  
**Kind**: property

The path separator.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var pathSeparator: String { get set }
```

#### Discussion

The default value of this property is `/`.

## See Also

- [func path() -> String](nsbrowser/path.md)
  Returns a string representing the browser’s current path.
- [func setPath(String) -> Bool](nsbrowser/setpath(_:).md)
  Sets the path to be displayed by the browser.
- [func path(toColumn: Int) -> String](nsbrowser/path(tocolumn:).md)
  Returns a string representing the path from the first column up to, but not including, the column at the given index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbrowser/pathseparator)*