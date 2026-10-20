# NSWhoseSpecifier.SubelementIdentifier

**Framework**: Foundation  
**Kind**: enum  
**Role**: Enumeration

`NSWhoseSpecifier` uses these constants to specify sub-elements within the collection of objects being tested that pass the specifier’s test.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
enum SubelementIdentifier
```

```c
enum NSWhoseSubelementIdentifier : NSUInteger;
```

#### Overview

These constants are used by [`startSubelementIdentifier`](./startsubelementidentifier.md), [`startSubelementIdentifier`](./startsubelementidentifier.md), [`endSubelementIdentifier`](./endsubelementidentifier.md), and [`endSubelementIdentifier`](./endsubelementidentifier.md).

## Topics

### Constants
- [NSWhoseSpecifier.SubelementIdentifier.indexSubelement](./subelementidentifier/indexsubelement.md)
  An element at a given index that meets the specifier test.
- [NSWhoseSpecifier.SubelementIdentifier.everySubelement](./subelementidentifier/everysubelement.md)
  Every element that meets the specifier test.
- [NSWhoseSpecifier.SubelementIdentifier.middleSubelement](./subelementidentifier/middlesubelement.md)
  The middle element that meets the specifier test.
- [NSWhoseSpecifier.SubelementIdentifier.randomSubelement](./subelementidentifier/randomsubelement.md)
  Any element that meets the specifier test.
- [NSWhoseSpecifier.SubelementIdentifier.noSubelement](./subelementidentifier/nosubelement.md)
  No sub-element met the specifier test. Valid only for specifying the end sub-element.; that is, there is no end, so consider all elements.
### Initializers
- [init?(rawValue: UInt)](./subelementidentifier/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nswhosespecifier/subelementidentifier)*