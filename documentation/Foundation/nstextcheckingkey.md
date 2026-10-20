# NSTextCheckingKey

**Framework**: Foundation  
**Kind**: struct  
**Role**: Structure

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
struct NSTextCheckingKey
```

```c
typedef NSString * NSTextCheckingKey;
```

## Topics

### Initializers
- [init(String)](./nstextcheckingkey/init%28_%29.md)
- [init(rawValue: String)](./nstextcheckingkey/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Constants
- [Keys for Transit Components](./keys-for-transit-components.md)
  The following constants identify the possible keys returned in the components dictionary.
- [Keys for Address Components](./keys-for-address-components.md)
  The following constants identify the possible keys returned in the [`addressComponents`](./nstextcheckingresult/addresscomponents.md) dictionary.
- [NSTextCheckingResult.CheckingType](./nstextcheckingresult/checkingtype.md)
  These constants specify the type of checking the methods should do. They are returned by [`resultType`](./nstextcheckingresult/resulttype.md).
- [typealias NSTextCheckingTypes](./nstextcheckingtypes.md)
  Defines the types of checking that are available. These values can be combined using the C-bitwise OR operator. The system supports its own internal types, and the user can extend those types by subclassing `NSTextCheckingResult` and adding their own custom types.
- [Anonymous](./api-1476845-anonymous.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nstextcheckingkey)*