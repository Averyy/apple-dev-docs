# textSelectionDataSource

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The data source associated with this selection navigation.

**Availability**:
- macOS 12.0+

## Declaration

```swift
weak var textSelectionDataSource: (any NSTextSelectionDataSource)? { get }
```

```objc
@property (weak, readonly) id<NSTextSelectionDataSource> textSelectionDataSource;
```

## See Also

### Accessing the data source
- [protocol NSTextSelectionDataSource](../nstextselectiondatasource.md)
  A set of methods that objects implement to provide data for, and manage text selections.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextselectionnavigation/textselectiondatasource)*