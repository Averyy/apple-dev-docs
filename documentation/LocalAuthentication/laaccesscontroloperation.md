# LAAccessControlOperation

**Framework**: Local Authentication  
**Kind**: enum

Operations to be evaluated for access control.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
enum LAAccessControlOperation
```

#### Overview

Use one of these values to specify the operation for which you want to evaluate an access control when calling the [`evaluateAccessControl(_:operation:localizedReason:reply:)`](lacontext/evaluateaccesscontrol(_:operation:localizedreason:reply:).md) method.

## Topics

### Constants
- [LAAccessControlOperation.createItem](laaccesscontroloperation/createitem.md)
  Specifies that access control is used for item creation.
- [LAAccessControlOperation.useItem](laaccesscontroloperation/useitem.md)
  Specifies that access control is used for accessing an existing item.
- [LAAccessControlOperation.createKey](laaccesscontroloperation/createkey.md)
  Specifies that access control is used for key creation.
- [LAAccessControlOperation.useKeySign](laaccesscontroloperation/usekeysign.md)
  Specifies that access control is used for accessing an existing key.
- [LAAccessControlOperation.useKeyDecrypt](laaccesscontroloperation/usekeydecrypt.md)
  Specifies that access control is used for data decryption using existing key.
- [LAAccessControlOperation.useKeyKeyExchange](laaccesscontroloperation/usekeykeyexchange.md)
  Specifies that access control is used for key exchange.
### Initializers
- [init?(rawValue: Int)](laaccesscontroloperation/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func evaluateAccessControl(SecAccessControl, operation: LAAccessControlOperation, localizedReason: String, reply: (Bool, (any Error)?) -> Void)](lacontext/evaluateaccesscontrol(_:operation:localizedreason:reply:).md)
  Evaluates an access control for a given operation.
- [var interactionNotAllowed: Bool](lacontext/interactionnotallowed.md)
  A Boolean value indicating whether authentication can be interactive.


---

*[View on Apple Developer](https://developer.apple.com/documentation/localauthentication/laaccesscontroloperation)*