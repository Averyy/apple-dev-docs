# rowClass

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The class used to create a new row in the “rows” binding.

**Availability**:
- macOS

## Declaration

```swift
var rowClass: AnyClass { get set }
```

```objc
@property (assign) Class rowClass;
```

## Discussion

The default is `NSMutableDictionary`.

## See Also

### Supporting Bindings
- [var rowTypeKeyPath: String](./rowtypekeypath.md)
  The key path for the row type.
- [var subrowsKeyPath: String](./subrowskeypath.md)
  The key path for the subrows.
- [var criteriaKeyPath: String](./criteriakeypath.md)
  The criteria key path.
- [var displayValuesKeyPath: String](./displayvalueskeypath.md)
  The display values key path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsruleeditor/rowclass)*