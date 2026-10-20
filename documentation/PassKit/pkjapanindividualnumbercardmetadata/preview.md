# preview

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: property  
**Role**: Instance Property

An object that contains information representing the pass for provisioning.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS
- visionOS 2.0+

## Declaration

```swift
var preview: PKAddPassMetadataPreview { get set }
```

```objc
@property (nonatomic, strong, readwrite, nonnull) PKAddPassMetadataPreview * preview;
```

## See Also

### Defining configuration
- [var authenticationPassword: String?](./authenticationpassword.md)
  A string that specifies the authentication password when provisioning the pass.
- [var signingPassword: String?](./signingpassword.md)
  A string that sets the signing password when you provision the pass.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkjapanindividualnumbercardmetadata/preview)*