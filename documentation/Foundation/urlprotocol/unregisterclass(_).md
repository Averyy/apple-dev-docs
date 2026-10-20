# unregisterClass(_:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Type Method

Unregisters the specified subclass of [`URLProtocol`](../urlprotocol.md).

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
class func unregisterClass(_ protocolClass: AnyClass)
```

```objc
+ (void) unregisterClass:(Class) protocolClass;
```

#### Discussion

After this method is invoked, `protocolClass` is no longer consulted by the URL loading system.

## Parameters

- `protocolClass`: The subclass of [`URLProtocol`](../urlprotocol.md) to unregister.

## See Also

### Registering and unregistering protocol classes
- [class func registerClass(AnyClass) -> Bool](./registerclass%28_%29.md)
  Attempts to register a subclass of [`URLProtocol`](../urlprotocol.md), making it visible to the URL loading system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlprotocol/unregisterclass(_:))*