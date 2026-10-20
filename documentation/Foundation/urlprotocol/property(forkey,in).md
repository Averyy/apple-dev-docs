# property(forKey:in:)

**Framework**: Foundation  
**Kind**: method

Fetches the property associated with the specified key in the specified request.

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
class func property(forKey key: String, in request: URLRequest) -> Any?
```

#### Return Value

The property associated with `key`, or `nil` if no property has been stored for `key`.

#### Discussion

Use this method to access protocol-specific information associated with [`URLRequest`](urlrequest.md) objects.

## Parameters

- `key`: The key of the desired property.
- `request`: The request whose properties are to be queried.

## See Also

- [class func setProperty(Any, forKey: String, in: NSMutableURLRequest)](urlprotocol/setproperty(_:forkey:in:).md)
  Sets the property associated with the specified key in the specified request.
- [class func removeProperty(forKey: String, in: NSMutableURLRequest)](urlprotocol/removeproperty(forkey:in:).md)
  Removes the property associated with the specified key in the specified request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlprotocol/property(forkey:in:))*