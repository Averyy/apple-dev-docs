# init(metadata:action:content:)

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: init

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst ?+
- visionOS ?+

## Declaration

```swift
nonisolated
init(metadata: [PKShareablePassMetadata], action: PKAddShareablePassConfigurationPrimaryAction, @ViewBuilder content: @escaping (AsyncShareablePassConfiguration<Content>.Result) -> Content)
```

## See Also

- [AsyncShareablePassConfiguration.Result](asyncshareablepassconfiguration/result.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/asyncshareablepassconfiguration/init(metadata:action:content:))*