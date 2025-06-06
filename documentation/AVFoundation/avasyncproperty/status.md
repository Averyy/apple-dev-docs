# AVAsyncProperty.Status

**Framework**: AVFoundation  
**Kind**: enum

Loaded status values for asynchronous properties.

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
@frozen
enum Status
```

## Mentions

- [Loading media data asynchronously](loading-media-data-asynchronously.md)

## Topics

### Status Values
- [AVAsyncProperty.Status.notYetLoaded](avasyncproperty/status/notyetloaded.md)
  The system hasn’t loaded a property value.
- [AVAsyncProperty.Status.loading](avasyncproperty/status/loading.md)
  The system is loading the property.
- [AVAsyncProperty.Status.loaded(_:)](avasyncproperty/status/loaded(_:).md)
  A property value is ready to use.
- [AVAsyncProperty.Status.failed(_:)](avasyncproperty/status/failed(_:).md)
  A property value fails to load.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avasyncproperty/status)*