# subrowsKeyPath

**Framework**: AppKit  
**Kind**: property

The key path for the subrows.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var subrowsKeyPath: String { get set }
```

#### Discussion

The key path is used to get the nested rows in the “rows” binding. The corresponding property should be an ordered to-many relationship containing additional bound row objects.

The default value is `@"subrows"`.

## See Also

- [var rowClass: AnyClass](nsruleeditor/rowclass.md)
  The class used to create a new row in the “rows” binding.
- [var rowTypeKeyPath: String](nsruleeditor/rowtypekeypath.md)
  The key path for the row type.
- [var criteriaKeyPath: String](nsruleeditor/criteriakeypath.md)
  The criteria key path.
- [var displayValuesKeyPath: String](nsruleeditor/displayvalueskeypath.md)
  The display values key path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsruleeditor/subrowskeypath)*