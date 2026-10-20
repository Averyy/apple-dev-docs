# init(metadata:action:content:)

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: init  
**Role**: Initializer

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS

## Declaration

```swift
nonisolated
init(metadata: [PKShareablePassMetadata], action: PKAddShareablePassConfigurationPrimaryAction, @ViewBuilder content: @escaping (AsyncShareablePassConfiguration<Content>.Result) -> Content)
```

## See Also

### Creating the configuration
- [AsyncShareablePassConfiguration.Result](./result.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/asyncshareablepassconfiguration/init(metadata:action:content:))*