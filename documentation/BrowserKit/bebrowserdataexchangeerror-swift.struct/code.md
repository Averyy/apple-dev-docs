# BEBrowserDataExchangeError.Code

**Framework**: BrowserKit  
**Kind**: enum

The types of data exchange errors that can occur.

**Availability**:
- iOS 26.4+ (Beta)
- iPadOS 26.4+ (Beta)

## Declaration

```swift
enum Code
```

#### Overview

The static [`BEBrowserDataExchangeError`](bebrowserdataexchangeerror-swift.struct.md) members are of this type.

## Topics

### Identifying error types
- [BEBrowserDataExchangeError.Code.export](bebrowserdataexchangeerror-swift.struct/code/export.md)
  An error that indicates a failure during the export operation.
- [BEBrowserDataExchangeError.Code.import](bebrowserdataexchangeerror-swift.struct/code/import.md)
  An error that indicates a failure during the import operation.
- [BEBrowserDataExchangeError.Code.unknown](bebrowserdataexchangeerror-swift.struct/code/unknown.md)
  An error that indicates an unexpected failure.
### Initializing an error code
- [init?(rawValue: Int)](bebrowserdataexchangeerror-swift.struct/code/init(rawvalue:).md)
  Initializes an error code with a value that represents the underlying type of error.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [static var export: BEBrowserDataExchangeError.Code](bebrowserdataexchangeerror-swift.struct/export.md)
  An error that indicates a failure during the export operation.
- [static var `import`: BEBrowserDataExchangeError.Code](bebrowserdataexchangeerror-swift.struct/import.md)
  An error that indicates a failure during the import operation.
- [static var unknown: BEBrowserDataExchangeError.Code](bebrowserdataexchangeerror-swift.struct/unknown.md)
  An error that indicates an unexpected failure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserkit/bebrowserdataexchangeerror-swift.struct/code)*