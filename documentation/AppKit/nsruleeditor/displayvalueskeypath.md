# displayValuesKeyPath

**Framework**: AppKit  
**Kind**: property

The display values key path.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var displayValuesKeyPath: String { get set }
```

#### Discussion

The key path is used to get the display values for a row in the “rows” binding. The display values are the objects returned by calling the delegate’s [`ruleEditor(_:displayValueForCriterion:inRow:)`](nsruleeditordelegate/ruleeditor(_:displayvalueforcriterion:inrow:).md) method for the specified row. The corresponding property is an ordered to-many relationship.

The default is `@"displayValues"`.

## See Also

- [var rowClass: AnyClass](nsruleeditor/rowclass.md)
  The class used to create a new row in the “rows” binding.
- [var rowTypeKeyPath: String](nsruleeditor/rowtypekeypath.md)
  The key path for the row type.
- [var subrowsKeyPath: String](nsruleeditor/subrowskeypath.md)
  The key path for the subrows.
- [var criteriaKeyPath: String](nsruleeditor/criteriakeypath.md)
  The criteria key path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsruleeditor/displayvalueskeypath)*