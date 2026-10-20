# registerClass(_:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Type Method

Attempts to register a subclass of [`URLProtocol`](../urlprotocol.md), making it visible to the URL loading system.

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

```objc
+ (BOOL) registerClass:(Class) protocolClass;
```

#### Return Value

[`true`](../../Swift/true.md) if the registration is successful, [`false`](../../Swift/false.md) otherwise. The only failure condition is if `protocolClass` is not a subclass of [`URLProtocol`](../urlprotocol.md).

#### Discussion

Register any custom [`URLProtocol`](../urlprotocol.md) subclasses prior to making URL requests. When the URL loading system begins to load a request, it tries to initialize each registered protocol class with the specified request. The first [`URLProtocol`](../urlprotocol.md) subclass to return [`true`](../../Swift/true.md) when sent a [`canInit(with:)`](./caninit%28with%29-76brg.md) message is used to load the request. There is no guarantee that all registered protocol classes will be consulted.

Classes are consulted in the reverse order of their registration. A similar design governs the process to create the canonical form of a request with [`canonicalRequest(for:)`](./canonicalrequest%28for%29.md).

## Parameters

- `protocolClass`: The subclass to register.

## See Also

### Registering and unregistering protocol classes
- [class func unregisterClass(AnyClass)](./unregisterclass%28_%29.md)
  Unregisters the specified subclass of [`URLProtocol`](../urlprotocol.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlprotocol/registerclass(_:))*