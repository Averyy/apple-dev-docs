# protocolCheckerWithTarget:protocol:

**Framework**: Foundation  
**Kind**: method  
**Role**: Type Method

Allocates and initializes an `NSProtocolChecker` instance that will forward any messages in `aProtocol` to `anObject`, the protocol checker’s target.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```objc
+ (instancetype) protocolCheckerWithTarget:(NSObject *) anObject protocol:(Protocol *) aProtocol;
```

## Discussion

Thus, the checker can be vended in lieu of `anObject` to restrict the messages that can be sent to `anObject`. Returns the new instance.

## See Also

### Related Documentation
- [Distributed Objects Programming Topics](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DistrObjects/DistrObjects.html#//apple_ref/doc/uid/10000102i)
### Creating a checker
- [init(target: NSObject, protocol: Protocol)](./init%28target,protocol%29.md)
  Initializes a newly allocated `NSProtocolChecker` instance that will forward any messages in `aProtocol` to `anObject`, the protocol checker’s target.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsprotocolchecker/protocolcheckerwithtarget:protocol:)*