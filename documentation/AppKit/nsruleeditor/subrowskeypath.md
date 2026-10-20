# subrowsKeyPath

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The key path for the subrows.

**Availability**:
- macOS

## Declaration

```swift
var subrowsKeyPath: String { get set }
```

```objc
@property (copy) NSString * subrowsKeyPath;
```

#### Discussion

The key path is used to get the nested rows in the “rows” binding. The corresponding property should be an ordered to-many relationship containing additional bound row objects.

The default value is `@"subrows"`.

## See Also

### Supporting Bindings
- [var rowClass: AnyClass](./rowclass.md)
  The class used to create a new row in the “rows” binding.
- [var rowTypeKeyPath: String](./rowtypekeypath.md)
  The key path for the row type.
- [var criteriaKeyPath: String](./criteriakeypath.md)
  The criteria key path.
- [var displayValuesKeyPath: String](./displayvalueskeypath.md)
  The display values key path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsruleeditor/subrowskeypath)*