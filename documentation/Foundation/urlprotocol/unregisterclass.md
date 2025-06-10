# unregisterClass(_:)

**Framework**: Foundation  
**Kind**: method

Unregisters the specified subclass of [`URLProtocol`](urlprotocol.md).

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

#### Discussion

After this method is invoked, `protocolClass` is no longer consulted by the URL loading system.

## Parameters

- `protocolClass`: The subclass of   to unregister.

## See Also

- [class func registerClass(AnyClass) -> Bool](urlprotocol/registerclass(_:).md)
  Attempts to register a subclass of [`URLProtocol`](urlprotocol.md), making it visible to the URL loading system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlprotocol/unregisterclass(_:))*