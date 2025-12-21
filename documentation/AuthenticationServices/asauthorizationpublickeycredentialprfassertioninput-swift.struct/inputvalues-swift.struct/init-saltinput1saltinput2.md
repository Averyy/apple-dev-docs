# init(saltInput1:saltInput2:)

**Framework**: Authentication Services  
**Kind**: init

Initializes an input values structure with the given salts.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
init(saltInput1: Data, saltInput2: Data? = nil)
```

## Parameters

- `saltInput1`: A salt for the hashing function.
- `saltInput2`: An optional second salt for the hashing function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationpublickeycredentialprfassertioninput-swift.struct/inputvalues-swift.struct/init(saltinput1:saltinput2:))*