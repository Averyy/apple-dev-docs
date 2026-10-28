# init(target:protocol:)

**Framework**: Foundation  
**Kind**: init  
**Role**: Initializer

Initializes a newly allocated `NSProtocolChecker` instance that will forward any messages in `aProtocol` to `anObject`, the protocol checker’s target.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
init(target anObject: NSObject, protocol aProtocol: Protocol)
```

```objc
- (instancetype) initWithTarget:(NSObject *) anObject protocol:(Protocol *) aProtocol;
```

## Discussion

Thus, the checker can be vended in lieu of `anObject` to restrict the messages that can be sent to `anObject`. If `anObject` is allowed to be freed or dereferenced by clients, the `free` method should be included in `aProtocol`.

## See Also

### Creating a checker
- [+ protocolCheckerWithTarget:protocol:](./protocolcheckerwithtarget_protocol_.md)
  Allocates and initializes an `NSProtocolChecker` instance that will forward any messages in `aProtocol` to `anObject`, the protocol checker’s target.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsprotocolchecker/init(target:protocol:))*