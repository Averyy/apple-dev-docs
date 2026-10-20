# init(for:)

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: init  
**Role**: Initializer

Instantiates a Suica pass properties object that contains the properties supported in the specified pass.

**Availability**:
- iOS 10.1+
- iPadOS 10.1+
- Mac Catalyst 13.1+
- macOS
- visionOS 1.0+
- watchOS 3.1+

## Declaration

```swift
convenience init?(for pass: PKPass)
```

```objc
+ (instancetype) passPropertiesForPass:(PKPass *) pass;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pksuicapassproperties/init(for:))*