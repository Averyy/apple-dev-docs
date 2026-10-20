# textSelectionDataSource

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The data source associated with this selection navigation.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- tvOS 15.0+
- visionOS 1.0+

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

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nstextselectionnavigation/textselectiondatasource)*