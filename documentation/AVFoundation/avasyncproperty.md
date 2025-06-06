# AVAsyncProperty

**Framework**: AVFoundation  
**Kind**: class

An asynchronous property that constrains its type and value.

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
class AVAsyncProperty<Root, Value>
```

## Mentions

- [Loading media data asynchronously](loading-media-data-asynchronously.md)

#### Overview

This class subclasses [`AVPartialAsyncProperty`](avpartialasyncproperty.md) to provide a type constraint on the property value.

## Topics

### Accessing the Status
- [AVAsyncProperty.Status](avasyncproperty/status.md)
  Loaded status values for asynchronous properties.

## Relationships

### Inherits From
- [AVPartialAsyncProperty](avpartialasyncproperty.md)
### Conforms To
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [protocol AVAsynchronousKeyValueLoading](avasynchronouskeyvalueloading.md)
  A protocol that defines the interface to load media data asynchronously.
- [class AVPartialAsyncProperty](avpartialasyncproperty.md)
  An asynchronous property that constrains its type.
- [class AVAnyAsyncProperty](avanyasyncproperty.md)
  A base class for asynchronous properties.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avasyncproperty)*