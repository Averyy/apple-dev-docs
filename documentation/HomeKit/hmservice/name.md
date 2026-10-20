# name

**Framework**: HomeKit  
**Kind**: property  
**Role**: Instance Property

The user specified name of the service.

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

Rename services by calling the [`updateName(_:completionHandler:)`](./updatename%28_,completionhandler%29.md) method with a value given by the user.

## See Also

### Identifying the service
- [func updateName(String, completionHandler: ((any Error)?) -> Void)](./updatename%28_,completionhandler%29.md)
  Updates the name of the service to the specified string.
- [var uniqueIdentifier: UUID](./uniqueidentifier.md)
  A unique identifier for the service.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmservice/name)*