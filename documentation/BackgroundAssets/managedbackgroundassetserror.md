# ManagedBackgroundAssetsError

**Framework**: Background Assets  
**Kind**: enum

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
- [ManagedBackgroundAssetsError.assetPackNotFound(withID:)](managedbackgroundassetserror/assetpacknotfound(withid:).md)
  An error that’s thrown when the system can’t find an asset pack with the given ID.
- [ManagedBackgroundAssetsError.fileNotFound(at:)](managedbackgroundassetserror/filenotfound(at:).md)
  An error that’s thrown when the system can’t find a file at the specified path.

## Relationships

### Conforms To
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Error](../Swift/Error.md)
- [LocalizedError](../Foundation/LocalizedError.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [let BAErrorDomain: String](baerrordomain.md)
- [enum BAErrorCode](baerrorcode.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundassets/managedbackgroundassetserror)*