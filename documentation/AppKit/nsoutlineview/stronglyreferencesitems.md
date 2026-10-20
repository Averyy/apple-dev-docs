# stronglyReferencesItems

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the outline view retains and releases the objects returned from its data source.

**Availability**:
- macOS 10.12+

## Declaration

```swift
var stronglyReferencesItems: Bool { get set }
```

```objc
@property BOOL stronglyReferencesItems;
```

#### Discussion

When the value of this property is [`true`](../../Swift/true.md), the outline view retains and releases the objects returned to it from [`dataSource`](./datasource.md). When the value is [`false`](../../Swift/false.md), the outline view treats the objects as opaque items and assumes that the client has a retain on them. The default value is [`true`](../../Swift/true.md) for applications linked on macOS 10.12 and later, and [`false`](../../Swift/false.md) for applications linked on earlier versions of macOS. If you require the legacy behavior and your app links in macOS 10.12 or later, the value of this property must be explicitly set to [`false`](../../Swift/false.md) in code, because it is not encoded in the nib. In general, this is required if the items themselves create a retain cycle.

## See Also

### Accessing the Data Source
- [var dataSource: (any NSOutlineViewDataSource)?](./datasource.md)
  The object that provides the data displayed by the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsoutlineview/stronglyreferencesitems)*