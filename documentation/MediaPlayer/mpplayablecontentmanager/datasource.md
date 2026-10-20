# dataSource

**Framework**: Media Player  
**Kind**: property  
**Role**: Instance Property

The data source provided by the app.

**Availability**:
- iOS 7.1+ - Deprecated in 14.0
- iPadOS 7.1+ - Deprecated in 14.0
- Mac Catalyst 13.1+ - Deprecated in 14.0
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: Use CarPlay framework

## Declaration

```swift
weak var dataSource: (any MPPlayableContentDataSource)? { get set }
```

```objc
@property (nonatomic, weak, nullable) id<MPPlayableContentDataSource> dataSource;
```

#### Discussion

This property ensures support for random access of media items through the [`MPPlayableContentDataSource`](../mpplayablecontentdatasource.md) protocol, whose methods are callable at any point during the app’s lifetime. Set this property as soon as the data is available.

## See Also

### Providing playable content
- [protocol MPPlayableContentDataSource](../mpplayablecontentdatasource.md)
  The data source providing media metadata to external media players so they can build user interfaces displaying your app’s content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpplayablecontentmanager/datasource)*