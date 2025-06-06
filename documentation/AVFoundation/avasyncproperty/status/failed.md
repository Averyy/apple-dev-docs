# AVAsyncProperty.Status.failed(_:)

**Framework**: AVFoundation  
**Kind**: case

A property value fails to load.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst ?+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
case failed(NSError)
```

## Parameters

- `error`: An error object that describes the failure.

## See Also

- [AVAsyncProperty.Status.notYetLoaded](avasyncproperty/status/notyetloaded.md)
  The system hasn’t loaded a property value.
- [AVAsyncProperty.Status.loading](avasyncproperty/status/loading.md)
  The system is loading the property.
- [AVAsyncProperty.Status.loaded(_:)](avasyncproperty/status/loaded(_:).md)
  A property value is ready to use.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avasyncproperty/status/failed(_:))*