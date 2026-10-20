# ManagedBackgroundAssetsError

**Framework**: Background Assets  
**Kind**: enum  
**Role**: Enumeration

An error for a managed asset pack.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
enum ManagedBackgroundAssetsError
```

## Topics

### Errors
- [ManagedBackgroundAssetsError.assetPackNotFound(withID:)](./managedbackgroundassetserror/assetpacknotfound%28withid%29.md)
  An error that’s thrown when the system can’t find an asset pack with the given ID.
- [ManagedBackgroundAssetsError.fileNotFound(at:)](./managedbackgroundassetserror/filenotfound%28at%29.md)
  An error that’s thrown when the system can’t find a file at the specified path.

## Relationships

### Conforms To
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Error](../Swift/error.md)
- [LocalizedError](../Foundation/localizederror.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Errors
- [let BAErrorDomain: String](./baerrordomain.md)
- [enum BAErrorCode](./baerrorcode.md)
- [AssetPackManager.LocalAvailabilityError](./assetpackmanager/localavailabilityerror.md)
  An error that provides information about local asset pack availability, distinguishing between successes and failures.


---

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundassets/managedbackgroundassetserror)*