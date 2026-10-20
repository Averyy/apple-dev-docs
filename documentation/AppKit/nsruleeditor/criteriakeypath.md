# criteriaKeyPath

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The criteria key path.

**Availability**:
- macOS

## Declaration

```swift
var criteriaKeyPath: String { get set }
```

```objc
@property (copy) NSString * criteriaKeyPath;
```

#### Discussion

The key path is used to get the criteria for a row in the “rows” binding. The criteria objects are the objects returned by calling the delegate’s [`ruleEditor(_:child:forCriterion:with:)`](../nsruleeditordelegate/ruleeditor%28_,child,forcriterion,with%29.md) method once for every child in the specified row. The corresponding property is an ordered to-many relationship.

The default value is `@"criteria"`.

## See Also

### Supporting Bindings
- [var rowClass: AnyClass](./rowclass.md)
  The class used to create a new row in the “rows” binding.
- [var rowTypeKeyPath: String](./rowtypekeypath.md)
  The key path for the row type.
- [var subrowsKeyPath: String](./subrowskeypath.md)
  The key path for the subrows.
- [var displayValuesKeyPath: String](./displayvalueskeypath.md)
  The display values key path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsruleeditor/criteriakeypath)*