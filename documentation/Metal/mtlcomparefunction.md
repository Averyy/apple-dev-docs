# MTLCompareFunction

**Framework**: Metal  
**Kind**: enum

Options used to specify how a sample compare operation should be performed on a depth texture.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
enum MTLCompareFunction
```

#### Overview

Whenever the comparison test passes, the incoming fragment is compared to the stored data at the specified location.

## Topics

### Compare function options
- [MTLCompareFunction.never](mtlcomparefunction/never.md)
  A new value never passes the comparison test.
- [MTLCompareFunction.less](mtlcomparefunction/less.md)
  A new value passes the comparison test if it is less than the existing value.
- [MTLCompareFunction.equal](mtlcomparefunction/equal.md)
  A new value passes the comparison test if it is equal to the existing value.
- [MTLCompareFunction.lessEqual](mtlcomparefunction/lessequal.md)
  A new value passes the comparison test if it is less than or equal to the existing value.
- [MTLCompareFunction.greater](mtlcomparefunction/greater.md)
  A new value passes the comparison test if it is greater than the existing value.
- [MTLCompareFunction.notEqual](mtlcomparefunction/notequal.md)
  A new value passes the comparison test if it is not equal to the existing value.
- [MTLCompareFunction.greaterEqual](mtlcomparefunction/greaterequal.md)
  A new value passes the comparison test if it is greater than or equal to the existing value.
- [MTLCompareFunction.always](mtlcomparefunction/always.md)
  A new value always passes the comparison test.
### Initializers
- [init?(rawValue: UInt)](mtlcomparefunction/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var compareFunction: MTLCompareFunction](mtlsamplerdescriptor/comparefunction.md)
  The sampler comparison function used when performing a sample compare operation on a depth texture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcomparefunction)*