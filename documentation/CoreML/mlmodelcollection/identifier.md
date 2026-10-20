# identifier

**Framework**: Core ML  
**Kind**: property  
**Role**: Instance Property

The name of the model collection, unique to the development team.

**Availability**:
- iOS 14.0+ - Deprecated in 17.4
- iPadOS 14.0+ - Deprecated in 17.4
- Mac Catalyst 14.0+ - Deprecated in 17.4
- visionOS 1.0+ - Deprecated in 1.1

> **Deprecated**: Use [Background Assets](../../BackgroundAssets/BackgroundAssets.md) or [`URLSession`](../../Foundation/urlsession.md) instead.

## Declaration

```swift
var identifier: String { get }
```

```objc
@property (nonatomic, copy, readonly) NSString * identifier;
```

## See Also

### Identifying a model collection
- [var deploymentID: String](./deploymentid.md)
  The unique identifier of the model collection’s deployment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlmodelcollection/identifier)*