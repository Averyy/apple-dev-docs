# second

**Framework**: Authentication Services  
**Kind**: property  
**Role**: Instance Property

A second symmetric key that’s unique to the passkey, and derives from the second input, if specified.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```objc
@property (nonatomic, readonly, nullable) NSData * second;
```

## See Also

### Accessing symmetric keys
- [first](./first.md)
  A symmetric key that’s unique to the passkey and derives from the first input, if specified.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationpublickeycredentialprfregistrationoutput-c.class/second)*