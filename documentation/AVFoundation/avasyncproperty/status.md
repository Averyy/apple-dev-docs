# AVAsyncProperty.Status

**Framework**: AVFoundation  
**Kind**: enum  
**Role**: Enumeration

Loaded status values for asynchronous properties.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
@frozen
enum Status
```

## Mentions

- [Loading media data asynchronously](../loading-media-data-asynchronously.md)

## Topics

### Status values
- [AVAsyncProperty.Status.notYetLoaded](./status/notyetloaded.md)
  The system hasn’t loaded a property value.
- [AVAsyncProperty.Status.loading](./status/loading.md)
  The system is loading the property.
- [AVAsyncProperty.Status.loaded(_:)](./status/loaded%28_%29.md)
  A property value is ready to use.
- [AVAsyncProperty.Status.failed(_:)](./status/failed%28_%29.md)
  A property value fails to load.

## Relationships

### Conforms To
- [Copyable](../../Swift/copyable.md)
- [CustomStringConvertible](../../Swift/customstringconvertible.md)
- [Equatable](../../Swift/equatable.md)
- [Escapable](../../Swift/escapable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avasyncproperty/status)*