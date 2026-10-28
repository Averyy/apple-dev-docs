# property(forKey:in:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Type Method

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

```objc
+ (id) propertyForKey:(NSString *) key inRequest:(NSURLRequest *) request;
```

## Return Value

The property associated with `key`, or `nil` if no property has been stored for `key`.

## Discussion

Use this method to access protocol-specific information associated with [`URLRequest`](../urlrequest.md) objects.

## Parameters

- `key`: The key of the desired property.
- `request`: The request whose properties are to be queried.

## See Also

### Getting and setting request properties
- [class func setProperty(Any, forKey: String, in: NSMutableURLRequest)](./setproperty%28_,forkey,in%29.md)
  Sets the property associated with the specified key in the specified request.
- [class func removeProperty(forKey: String, in: NSMutableURLRequest)](./removeproperty%28forkey,in%29.md)
  Removes the property associated with the specified key in the specified request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlprotocol/property(forkey:in:))*