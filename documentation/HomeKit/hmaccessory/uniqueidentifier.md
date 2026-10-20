# uniqueIdentifier

**Framework**: HomeKit  
**Kind**: property  
**Role**: Instance Property

A unique identifier for the accessory.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var uniqueIdentifier: UUID { get }
```

```objc
@property (nonatomic, copy, readonly) NSUUID * uniqueIdentifier;
```

## See Also

### Identifying an Accessory
- [var name: String](./name.md)
  The name of the accessory.
- [func updateName(String, completionHandler: ((any Error)?) -> Void)](./updatename%28_,completionhandler%29.md)
  Changes the name of the accessory.
- [var identifier: UUID](./identifier.md)
  A unique identifier for the accessory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmaccessory/uniqueidentifier)*