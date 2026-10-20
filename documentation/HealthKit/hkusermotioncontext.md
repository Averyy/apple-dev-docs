# HKUserMotionContext

**Framework**: HealthKit  
**Kind**: enum  
**Role**: Enumeration

The type of motion performed during the sample.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
enum HKUserMotionContext
```

```c
enum HKUserMotionContext : NSInteger;
```

## Topics

### Motion contexts
- [HKUserMotionContext.notSet](./hkusermotioncontext/notset.md)
  The person’s motion was not specified.
- [HKUserMotionContext.active](./hkusermotioncontext/active.md)
  The person was active during the sample.
- [HKUserMotionContext.stationary](./hkusermotioncontext/stationary.md)
  The person was stationary during the sample.
### Initializers
- [init?(rawValue: Int)](./hkusermotioncontext/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkusermotioncontext)*