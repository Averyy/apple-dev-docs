# identifier

**Framework**: HomeKit  
**Kind**: property  
**Role**: Instance Property

A unique identifier for the accessory.

**Availability**:
- iOS 8.0+ - Deprecated in 9.0
- iPadOS 8.0+ - Deprecated in 9.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: Use [`uniqueIdentifier`](./uniqueidentifier.md) instead.

## Declaration

```swift
var identifier: UUID { get }
```

```objc
@property (nonatomic, copy, readonly) NSUUID * identifier;
```

#### Discussion

An identifier is stable for as long as an accessory is in a home. If an accessory is removed from a home, it will get a new identifier when it is next added to a home.

## See Also

### Identifying an Accessory
- [var name: String](./name.md)
  The name of the accessory.
- [func updateName(String, completionHandler: ((any Error)?) -> Void)](./updatename%28_,completionhandler%29.md)
  Changes the name of the accessory.
- [var uniqueIdentifier: UUID](./uniqueidentifier.md)
  A unique identifier for the accessory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmaccessory/identifier)*