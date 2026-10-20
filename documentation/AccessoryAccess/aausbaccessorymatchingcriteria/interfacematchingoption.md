# AAUSBAccessoryMatchingCriteria.InterfaceMatchingOption

**Framework**: Accessory Access  
**Kind**: enum  
**Role**: Enumeration

Values that represent options for performing interface matching using interface matching criteria.

**Availability**:
- macOS 27.0+

## Declaration

```swift
enum InterfaceMatchingOption
```

```c
enum AAUSBAccessoryMatchingCriteriaInterfaceMatchingOption : NSInteger;
```

## Topics

- [init?(rawValue: Int)](./interfacematchingoption/init%28rawvalue%29.md)
  Initializes a new interface matching option with the provided value.
- [AAUSBAccessoryMatchingCriteria.InterfaceMatchingOption.matchAll](./interfacematchingoption/matchall.md)
  A value that indicates the match needs to be all inclusive of the provided interface criteria.
- [AAUSBAccessoryMatchingCriteria.InterfaceMatchingOption.matchAny](./interfacematchingoption/matchany.md)
  A value that indicates that the match needs to cover at least one of the provided interface criteria.

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessoryaccess/aausbaccessorymatchingcriteria/interfacematchingoption)*