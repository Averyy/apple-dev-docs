# BEBrowserDataExchangeError

**Framework**: BrowserKit  
**Kind**: struct

An error that occurs during browser data import or export operations.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+

## Declaration

```swift
struct BEBrowserDataExchangeError
```

#### Overview

This error type provides codes for failures during the transfer of browsing data, including import failures, export failures, and unknown errors.

## Topics

### Identifying error types
- [BEBrowserDataExchangeError.Code](bebrowserdataexchangeerror-swift.struct/code.md)
  The types of data exchange errors that can occur.
- [static var export: BEBrowserDataExchangeError.Code](bebrowserdataexchangeerror-swift.struct/export.md)
  An error that indicates a failure during the export operation.
- [static var `import`: BEBrowserDataExchangeError.Code](bebrowserdataexchangeerror-swift.struct/import.md)
  An error that indicates a failure during the import operation.
- [static var unknown: BEBrowserDataExchangeError.Code](bebrowserdataexchangeerror-swift.struct/unknown.md)
  An error that indicates an unexpected failure.
### Getting error information
- [static var errorDomain: String](bebrowserdataexchangeerror-swift.struct/errordomain.md)
  A constant that identifies the error domain for browser data exchange errors.

## Relationships

### Conforms To
- [CustomNSError](../foundation/customnserror.md)
- [Equatable](../swift/equatable.md)
- [Error](../swift/error.md)
- [Hashable](../swift/hashable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [let BEBrowserDataExchangeErrorDomain: String](bebrowserdataexchangeerrordomain.md)
  A constant that identifies the error domain for browser data exchange errors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserkit/bebrowserdataexchangeerror-swift.struct)*