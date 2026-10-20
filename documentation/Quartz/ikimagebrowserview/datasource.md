# dataSource

**Framework**: Quartz  
**Kind**: property  
**Role**: Instance Property

Returns the data source of the receiver.

**Availability**:
- macOS 10.4+

## Declaration

```swift
@IBOutlet
unowned(unsafe) var dataSource: AnyObject! { get set }
```

```objc
@property (assign) id dataSource;
```

#### Return Value

The data source (`IKImageBrowserDataSource`). The data source is not retained by the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/ikimagebrowserview/datasource)*