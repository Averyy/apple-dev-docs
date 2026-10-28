# serviceType

**Framework**: Social  
**Kind**: property  
**Role**: Instance Property

Specifies the social-networking service.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+

## Declaration

```swift
var serviceType: String! { get }
```

```objc
@property (nonatomic, readonly) NSString * serviceType;
```

## Discussion

The value of this property is set when you initialize a social compose view controller in [`init(forServiceType:)`](./init%28forservicetype%29.md). Each social view controller you present is connected to only one social service at a time. Use this property to check which service your social view controller has specified. For a list of possible values, see Service Type Constants.

## See Also

### Checking the Social Service Type
- [class func isAvailable(forServiceType: String!) -> Bool](./isavailable%28forservicetype%29.md)
  Returns A Boolean value that indicates whether you can send a request for a particular service type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/social/slcomposeviewcontroller/servicetype)*