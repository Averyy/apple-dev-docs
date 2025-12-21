# MLWritable

**Framework**: Core ML  
**Kind**: protocol

A set of methods that saves a machine learning type to the file system.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
protocol MLWritable : NSObjectProtocol
```

#### Overview

You use [`MLWritable`](mlwritable.md) to save any [`MLModel`](mlmodel.md) instance that adopts the protocol to the file system.

## Topics

### Saving to a file
- [func write(to: URL) throws](mlwritable/write(to:).md)
  Exports a machine learning file to the file system.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [var model: any MLModel & MLWritable](mlupdatecontext/model.md)
  The underlying Core ML model stored in memory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlwritable)*