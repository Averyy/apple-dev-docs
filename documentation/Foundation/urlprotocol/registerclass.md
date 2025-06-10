# registerClass(_:)

**Framework**: Foundation  
**Kind**: method

Attempts to register a subclass of [`URLProtocol`](urlprotocol.md), making it visible to the URL loading system.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.2+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class func registerClass(_ protocolClass: AnyClass) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the registration is successful, [`false`](https://developer.apple.com/documentation/swift/false) otherwise. The only failure condition is if `protocolClass` is not a subclass of [`URLProtocol`](urlprotocol.md).

#### Discussion

Register any custom [`URLProtocol`](urlprotocol.md) subclasses prior to making URL requests. When the URL loading system begins to load a request, it tries to initialize each registered protocol class with the specified request. The first [`URLProtocol`](urlprotocol.md) subclass to return [`true`](https://developer.apple.com/documentation/swift/true) when sent a [`canInit(with:)`](urlprotocol/caninit(with:)-76brg.md) message is used to load the request. There is no guarantee that all registered protocol classes will be consulted.

Classes are consulted in the reverse order of their registration. A similar design governs the process to create the canonical form of a request with [`canonicalRequest(for:)`](urlprotocol/canonicalrequest(for:).md).

## Parameters

- `protocolClass`: The subclass to register.

## See Also

- [class func unregisterClass(AnyClass)](urlprotocol/unregisterclass(_:).md)
  Unregisters the specified subclass of [`URLProtocol`](urlprotocol.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlprotocol/registerclass(_:))*