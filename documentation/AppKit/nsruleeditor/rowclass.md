# rowClass

**Framework**: AppKit  
**Kind**: property

The class used to create a new row in the “rows” binding.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var rowClass: AnyClass { get set }
```

#### Discussion

The default is `NSMutableDictionary`.

## See Also

- [var rowTypeKeyPath: String](nsruleeditor/rowtypekeypath.md)
  The key path for the row type.
- [var subrowsKeyPath: String](nsruleeditor/subrowskeypath.md)
  The key path for the subrows.
- [var criteriaKeyPath: String](nsruleeditor/criteriakeypath.md)
  The criteria key path.
- [var displayValuesKeyPath: String](nsruleeditor/displayvalueskeypath.md)
  The display values key path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsruleeditor/rowclass)*