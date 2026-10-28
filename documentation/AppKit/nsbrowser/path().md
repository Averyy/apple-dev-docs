# path()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns a string representing the browser’s current path.

**Availability**:
- macOS

## Declaration

```swift
func path() -> String
```

```objc
- (NSString *) path;
```

## Return Value

The path representing the current selection. The components of this path are separated with the string returned by [`pathSeparator`](./pathseparator.md).

## Discussion

Invoking this method is equivalent to invoking [`path(toColumn:)`](./path%28tocolumn%29.md) for all columns.

## See Also

### Managing the Path
- [func setPath(String) -> Bool](./setpath%28_%29.md)
  Sets the path to be displayed by the browser.
- [func path(toColumn: Int) -> String](./path%28tocolumn%29.md)
  Returns a string representing the path from the first column up to, but not including, the column at the given index.
- [var pathSeparator: String](./pathseparator.md)
  The path separator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbrowser/path())*