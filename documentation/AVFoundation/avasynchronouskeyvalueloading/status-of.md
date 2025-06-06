# status(of:)

**Framework**: AVFoundation  
**Kind**: method

Returns a value that indicates the loaded status of a property.

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
func status<T>(of property: AVAsyncProperty<Self, T>) -> AVAsyncProperty<Self, T>.Status
```

## Mentions

- [Loading media data asynchronously](loading-media-data-asynchronously.md)

#### Return Value

A status value.

#### Discussion

A status of [`AVAsyncProperty.Status.loaded(_:)`](avasyncproperty/status/loaded(_:).md) provides the property value, and a status of [`AVAsyncProperty.Status.failed(_:)`](avasyncproperty/status/failed(_:).md) provides an error that describes the failure.

## Parameters

- `property`: A property identifier with a status to check.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avasynchronouskeyvalueloading/status(of:))*