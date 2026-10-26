# initWithSaltInput1:saltInput2:

**Framework**: Authentication Services  
**Kind**: method  
**Role**: Instance Method

Initializes an input values object with the given salts.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```objc
- (instancetype) initWithSaltInput1:(NSData *) saltInput1 saltInput2:(NSData *) saltInput2;
```

## Parameters

- `saltInput1`: A salt for the hashing function.
- `saltInput2`: An optional second salt for the hashing function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationpublickeycredentialprfassertioninputvalues/initwithsaltinput1:saltinput2:)*