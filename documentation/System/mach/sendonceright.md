# Mach.SendOnceRight

**Framework**: System  
**Kind**: struct

The MachPortRight type used to manage a send-once right.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+
- macOS 14.4+
- tvOS 17.4+
- visionOS 1.0+
- watchOS 10.4+

## Declaration

```swift
@frozen
struct SendOnceRight
```

#### Overview

Send-once rights are the most restrictive type of Mach port rights. They cannot create other rights, and are consumed upon use.

Upon destruction a send-once notification will be sent to the receiving end.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Copyable](../Swift/Copyable.md)
- [MachPortRight](machportright.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/system/mach/sendonceright)*