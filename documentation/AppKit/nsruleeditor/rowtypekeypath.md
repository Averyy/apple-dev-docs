# rowTypeKeyPath

**Framework**: AppKit  
**Kind**: property

The key path for the row type.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var rowTypeKeyPath: String { get set }
```

#### Discussion

The key path is used to get the row type in the “rows” binding. The corresponding property should be a number that specifies an `NSRuleEditorRowType` value (see `Row Types`).

The default value is `@"rowType"`.

## See Also

- [var rowClass: AnyClass](nsruleeditor/rowclass.md)
  The class used to create a new row in the “rows” binding.
- [var subrowsKeyPath: String](nsruleeditor/subrowskeypath.md)
  The key path for the subrows.
- [var criteriaKeyPath: String](nsruleeditor/criteriakeypath.md)
  The criteria key path.
- [var displayValuesKeyPath: String](nsruleeditor/displayvalueskeypath.md)
  The display values key path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsruleeditor/rowtypekeypath)*