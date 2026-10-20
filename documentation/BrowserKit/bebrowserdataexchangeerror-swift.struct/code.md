# BEBrowserDataExchangeError.Code

**Framework**: BrowserKit  
**Kind**: enum  
**Role**: Enumeration

The types of data exchange errors that can occur.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+

## Declaration

```swift
enum Code
```

```c
enum BEBrowserDataExchangeError : NSInteger;
```

#### Overview

The static [`BEBrowserDataExchangeError`](../bebrowserdataexchangeerror-swift.struct.md) members are of this type.

## Topics

### Identifying error types
- [BEBrowserDataExchangeError.Code.export](./code/export.md)
  An error that indicates a failure during the export operation.
- [BEBrowserDataExchangeError.Code.import](./code/import.md)
  An error that indicates a failure during the import operation.
- [BEBrowserDataExchangeError.Code.unknown](./code/unknown.md)
  An error that indicates an unexpected failure.
### Initializing an error code
- [init?(rawValue: Int)](./code/init%28rawvalue%29.md)
  Initializes an error code with a value that represents the underlying type of error.

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Identifying error types
- [static var export: BEBrowserDataExchangeError.Code](./export.md)
  An error that indicates a failure during the export operation.
- [static var `import`: BEBrowserDataExchangeError.Code](./import.md)
  An error that indicates a failure during the import operation.
- [static var unknown: BEBrowserDataExchangeError.Code](./unknown.md)
  An error that indicates an unexpected failure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserkit/bebrowserdataexchangeerror-swift.struct/code)*