# dataSource

**Framework**: Quartz  
**Kind**: property

Returns the data source of the receiver.

**Availability**:
- macOS 10.4+

## Declaration

```swift
@IBOutlet
@MainActor unowned(unsafe) var dataSource: AnyObject! { get set }
```

#### Return Value

The data source (`IKImageBrowserDataSource`). The data source is not retained by the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/ikimagebrowserview/datasource)*