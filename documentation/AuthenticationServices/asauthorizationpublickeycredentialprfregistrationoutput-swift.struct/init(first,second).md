# init(first:second:)

**Framework**: Authentication Services  
**Kind**: init  
**Role**: Initializer

Initializes an object representing the outputs of the web authentication PRF extension.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
init(first: SymmetricKey, second: SymmetricKey?)
```

#### Discussion

Call this method only if the registration request includes input values. Otherwise, use [`supported`](./supported.md) or [`unsupported`](./unsupported.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationpublickeycredentialprfregistrationoutput-swift.struct/init(first:second:))*