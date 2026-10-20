# pathSeparator

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The path separator.

**Availability**:
- macOS

## Declaration

```swift
var pathSeparator: String { get set }
```

```objc
@property (copy) NSString * pathSeparator;
```

#### Discussion

The default value of this property is `/`.

## See Also

### Managing the Path
- [func path() -> String](./path%28%29.md)
  Returns a string representing the browser’s current path.
- [func setPath(String) -> Bool](./setpath%28_%29.md)
  Sets the path to be displayed by the browser.
- [func path(toColumn: Int) -> String](./path%28tocolumn%29.md)
  Returns a string representing the path from the first column up to, but not including, the column at the given index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbrowser/pathseparator)*