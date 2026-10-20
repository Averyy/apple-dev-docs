# name

**Framework**: HomeKit  
**Kind**: property  
**Role**: Instance Property

The name of the accessory.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var name: String { get }
```

```objc
@property (nonatomic, copy, readonly) NSString * name;
```

#### Discussion

Use the [`updateName(_:completionHandler:)`](./updatename%28_,completionhandler%29.md) method to change the name to a value chosen by the user.

## See Also

### Identifying an Accessory
- [func updateName(String, completionHandler: ((any Error)?) -> Void)](./updatename%28_,completionhandler%29.md)
  Changes the name of the accessory.
- [var uniqueIdentifier: UUID](./uniqueidentifier.md)
  A unique identifier for the accessory.
- [var identifier: UUID](./identifier.md)
  A unique identifier for the accessory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmaccessory/name)*