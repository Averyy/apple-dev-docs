# dataSource

**Framework**: Media Player  
**Kind**: property

The data source provided by the app.

**Availability**:
- iOS 7.1+
- iPadOS 7.1+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
weak var dataSource: (any MPPlayableContentDataSource)? { get set }
```

#### Discussion

This property ensures support for random access of media items through the [`MPPlayableContentDataSource`](mpplayablecontentdatasource.md) protocol, whose methods are callable at any point during the app’s lifetime. Set this property as soon as the data is available.

## See Also

- [protocol MPPlayableContentDataSource](mpplayablecontentdatasource.md)
  The data source providing media metadata to external media players so they can build user interfaces displaying your app’s content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpplayablecontentmanager/datasource)*