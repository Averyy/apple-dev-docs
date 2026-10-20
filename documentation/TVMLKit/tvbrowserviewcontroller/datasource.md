# dataSource

**Framework**: TVMLKit  
**Kind**: property  
**Role**: Instance Property

The object that provides data to the full-screen browser.

**Availability**:
- tvOS 13.0+

## Declaration

```swift
weak var dataSource: (any TVBrowserViewControllerDataSource)? { get set }
```

```objc
@property (nonatomic, weak) id<TVBrowserViewControllerDataSource> dataSource;
```

## See Also

### Providing the Browser’s Data
- [protocol TVBrowserViewControllerDataSource](../tvbrowserviewcontrollerdatasource.md)
  Methods adopted by the object you use to represent the browser view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmlkit/tvbrowserviewcontroller/datasource)*