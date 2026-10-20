# deploymentID

**Framework**: Core ML  
**Kind**: property  
**Role**: Instance Property

The unique identifier of the model collection’s deployment.

**Availability**:
- iOS 14.0+ - Deprecated in 17.4
- iPadOS 14.0+ - Deprecated in 17.4
- Mac Catalyst 14.0+ - Deprecated in 17.4
- visionOS 1.0+ - Deprecated in 1.1

> **Deprecated**: Use [Background Assets](../../BackgroundAssets/BackgroundAssets.md) or [`URLSession`](../../Foundation/urlsession.md) instead.

## Declaration

```swift
var deploymentID: String { get }
```

```objc
@property (nonatomic, copy, readonly) NSString * deploymentID;
```

## See Also

### Identifying a model collection
- [var identifier: String](./identifier.md)
  The name of the model collection, unique to the development team.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlmodelcollection/deploymentid)*