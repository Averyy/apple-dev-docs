# QualityOfService

**Framework**: Foundation  
**Kind**: enum

Constants that indicate the nature and importance of work to the system.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
enum QualityOfService
```

#### Overview

Work with higher quality of service classes receive more resources than work with lower quality of service classes whenever there’s resource contention.

## Topics

### Constants
- [QualityOfService.userInteractive](qualityofservice/userinteractive.md)
- [QualityOfService.userInitiated](qualityofservice/userinitiated.md)
- [QualityOfService.utility](qualityofservice/utility.md)
- [QualityOfService.background](qualityofservice/background.md)
- [QualityOfService.default](qualityofservice/default.md)
### Initializers
- [init?(rawValue: Int)](qualityofservice/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Operation.QueuePriority](operation/queuepriority-swift.enum.md)
  These constants let you prioritize the order in which operations execute.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/qualityofservice)*