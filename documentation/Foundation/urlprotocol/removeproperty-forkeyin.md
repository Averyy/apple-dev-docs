# removeProperty(forKey:in:)

**Framework**: Foundation  
**Kind**: method

Removes the property associated with the specified key in the specified request.

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
class func removeProperty(forKey key: String, in request: NSMutableURLRequest)
```

#### Discussion

This method is used to provide an interface for protocol implementors to customize protocol-specific information associated with [`URLRequest`](urlrequest.md) objects, or [`NSMutableURLRequest`](nsmutableurlrequest.md) objects in Objective-C.

## Parameters

- `key`: The key whose value should be removed.
- `request`: The request from which to remove the property value.

## See Also

- [class func property(forKey: String, in: URLRequest) -> Any?](urlprotocol/property(forkey:in:).md)
  Fetches the property associated with the specified key in the specified request.
- [class func setProperty(Any, forKey: String, in: NSMutableURLRequest)](urlprotocol/setproperty(_:forkey:in:).md)
  Sets the property associated with the specified key in the specified request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlprotocol/removeproperty(forkey:in:))*