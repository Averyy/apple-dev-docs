# criteriaKeyPath

**Framework**: AppKit  
**Kind**: property

The criteria key path.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var criteriaKeyPath: String { get set }
```

#### Discussion

The key path is used to get the criteria for a row in the “rows” binding. The criteria objects are the objects returned by calling the delegate’s [`ruleEditor(_:child:forCriterion:with:)`](nsruleeditordelegate/ruleeditor(_:child:forcriterion:with:).md) method once for every child in the specified row. The corresponding property is an ordered to-many relationship.

The default value is `@"criteria"`.

## See Also

- [var rowClass: AnyClass](nsruleeditor/rowclass.md)
  The class used to create a new row in the “rows” binding.
- [var rowTypeKeyPath: String](nsruleeditor/rowtypekeypath.md)
  The key path for the row type.
- [var subrowsKeyPath: String](nsruleeditor/subrowskeypath.md)
  The key path for the subrows.
- [var displayValuesKeyPath: String](nsruleeditor/displayvalueskeypath.md)
  The display values key path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsruleeditor/criteriakeypath)*