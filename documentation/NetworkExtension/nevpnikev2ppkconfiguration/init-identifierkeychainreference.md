# init(identifier:keychainReference:)

**Framework**: Network Extension  
**Kind**: init

Initializes a quantum-secure pre-shared key (PPK) configuration.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
init(identifier: String, keychainReference: Data)
```

## Parameters

- `identifier`: The identifier for the PPK.
- `keychainReference`: A persistent reference to a keychain item with the class   that contains the PPK.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nevpnikev2ppkconfiguration/init(identifier:keychainreference:))*