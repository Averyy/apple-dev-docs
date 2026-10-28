# rowTypeKeyPath

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The key path for the row type.

**Availability**:
- macOS

## Declaration

```swift
var rowTypeKeyPath: String { get set }
```

```objc
@property (copy) NSString * rowTypeKeyPath;
```

## Discussion

The key path is used to get the row type in the “rows” binding. The corresponding property should be a number that specifies an `NSRuleEditorRowType` value (see `Row Types`).

The default value is `@"rowType"`.

## See Also

### Supporting Bindings
- [var rowClass: AnyClass](./rowclass.md)
  The class used to create a new row in the “rows” binding.
- [var subrowsKeyPath: String](./subrowskeypath.md)
  The key path for the subrows.
- [var criteriaKeyPath: String](./criteriakeypath.md)
  The criteria key path.
- [var displayValuesKeyPath: String](./displayvalueskeypath.md)
  The display values key path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsruleeditor/rowtypekeypath)*