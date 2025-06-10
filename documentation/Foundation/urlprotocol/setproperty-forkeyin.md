# setProperty(_:forKey:in:)

**Framework**: Foundation  
**Kind**: method

Sets the property associated with the specified key in the specified request.

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
class func setProperty(_ value: Any, forKey key: String, in request: NSMutableURLRequest)
```

#### Discussion

Use this method to provide an interface for protocol implementors to customize protocol-specific information associated with [`URLRequest`](urlrequest.md) objects.

## Parameters

- `value`: The value to set for the specified property.
- `key`: The key for the specified property.
- `request`: The request for which to create the property.

## See Also

- [class func property(forKey: String, in: URLRequest) -> Any?](urlprotocol/property(forkey:in:).md)
  Fetches the property associated with the specified key in the specified request.
- [class func removeProperty(forKey: String, in: NSMutableURLRequest)](urlprotocol/removeproperty(forkey:in:).md)
  Removes the property associated with the specified key in the specified request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlprotocol/setproperty(_:forkey:in:))*