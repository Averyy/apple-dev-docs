# setProperty(_:forKey:in:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Type Method

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

```objc
+ (void) setProperty:(id) value forKey:(NSString *) key inRequest:(NSMutableURLRequest *) request;
```

#### Discussion

Use this method to provide an interface for protocol implementors to customize protocol-specific information associated with [`URLRequest`](../urlrequest.md) objects.

## Parameters

- `value`: The value to set for the specified property.
- `key`: The key for the specified property.
- `request`: The request for which to create the property.

## See Also

### Getting and setting request properties
- [class func property(forKey: String, in: URLRequest) -> Any?](./property%28forkey,in%29.md)
  Fetches the property associated with the specified key in the specified request.
- [class func removeProperty(forKey: String, in: NSMutableURLRequest)](./removeproperty%28forkey,in%29.md)
  Removes the property associated with the specified key in the specified request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlprotocol/setproperty(_:forkey:in:))*