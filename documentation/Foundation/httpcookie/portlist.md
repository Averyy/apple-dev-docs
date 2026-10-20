# portList

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

The cookie’s port list.

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
var portList: [NSNumber]? { get }
```

```objc
@property (copy, readonly, nullable) NSArray<NSNumber *> * portList;
```

#### Discussion

The list of ports for the cookie, returned as an array of `NSNumber` objects containing integers. If the cookie has no port list, the value of this property is `nil` and the cookie will be sent to any port. Otherwise, the cookie is only sent to ports specified in the port list.

## See Also

### Getting cookie host properties
- [var domain: String](./domain.md)
  The domain of the cookie.
- [var path: String](./path.md)
  The cookie’s path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/httpcookie/portlist)*