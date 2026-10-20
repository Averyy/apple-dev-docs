# path(toColumn:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns a string representing the path from the first column up to, but not including, the column at the given index.

**Availability**:
- macOS

## Declaration

```swift
func path(toColumn column: Int) -> String
```

```objc
- (NSString *) pathToColumn:(NSInteger) column;
```

#### Return Value

The path of the current selection up to, but not including, the specified column. The components of this path are separated with the string returned by [`pathSeparator`](./pathseparator.md).

## Parameters

- `column`: The index of the column at which the path stops.

## See Also

### Managing the Path
- [func path() -> String](./path%28%29.md)
  Returns a string representing the browser’s current path.
- [func setPath(String) -> Bool](./setpath%28_%29.md)
  Sets the path to be displayed by the browser.
- [var pathSeparator: String](./pathseparator.md)
  The path separator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbrowser/path(tocolumn:))*