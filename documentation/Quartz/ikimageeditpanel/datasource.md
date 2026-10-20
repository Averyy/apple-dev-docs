# dataSource

**Framework**: Quartz  
**Kind**: property  
**Role**: Instance Property

Specifies the edit panel’s dataSource.

**Availability**:
- macOS 10.5+

## Declaration

```swift
unowned(unsafe) var dataSource: (any IKImageEditPanelDataSource)! { get set }
```

```objc
@property (assign) id<IKImageEditPanelDataSource> dataSource;
```

## See Also

### Getting, Setting, and Reloading Data
- [func reloadData()](./reloaddata%28%29.md)
  Reloads the data from the data associated with an image editing panel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/ikimageeditpanel/datasource)*