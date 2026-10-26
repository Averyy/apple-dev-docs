# delegate

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

The receiver’s delegate.

**Availability**:
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.0+ - Deprecated in 10.13

## Declaration

```objc
@property (assign, nullable) id<NSConnectionDelegate> delegate;
```

#### Discussion

A connection’s delegate can process incoming messages itself instead of letting `NSConnection` object handle them. The delegate can also authenticate messages and accept, deny, or modify new connections.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsconnection/delegate-c.property)*