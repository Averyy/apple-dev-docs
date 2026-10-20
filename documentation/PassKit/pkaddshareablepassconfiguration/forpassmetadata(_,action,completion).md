# forPassMetadata(_:action:completion:)

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: method  
**Role**: Type Method

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS
- visionOS 1.0+

## Declaration

```swift
class func forPassMetadata(_ passMetadata: [PKShareablePassMetadata], action: PKAddShareablePassConfigurationPrimaryAction, completion: @escaping @Sendable (PKAddShareablePassConfiguration?, (any Error)?) -> Void)
```

```swift
class func forPassMetadata(_ passMetadata: [PKShareablePassMetadata], action: PKAddShareablePassConfigurationPrimaryAction) async throws -> PKAddShareablePassConfiguration
```

```objc
+ (void) configurationForPassMetadata:(NSArray<PKShareablePassMetadata *> *) passMetadata primaryAction:(PKAddShareablePassConfigurationPrimaryAction) action completion:(void (^)(PKAddShareablePassConfiguration *shareableCredentialConfiguration, NSError *error)) completion;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkaddshareablepassconfiguration/forpassmetadata(_:action:completion:))*