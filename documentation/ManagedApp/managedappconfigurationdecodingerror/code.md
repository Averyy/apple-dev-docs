# code

**Framework**: ManagedApp  
**Kind**: property  
**Required**: Yes

An app-specific error code that identifies a configuration issue.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- macOS 27.0+ (Beta)
- visionOS 2.4+

## Declaration

```swift
var code: ManagedAppConfigurationDecodingErrorCode { get set }
```

## Mentions

- [Specifying and decoding a configuration](specifying-and-decoding-a-configuration.md)

#### Discussion

The system reserves values equal to or greater than `ManagedAppConfigurationDecodingErrorCodes.firstReserved`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/managedapp/managedappconfigurationdecodingerror/code)*