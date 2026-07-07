# NSFileProviderNamespacePolicy.materializeEagerly

**Framework**: File Provider  
**Kind**: case

Download this folder eagerly, make sure it’s always fully enumerated Keep downloading remote updates eagerly. Prevent eviction on low disk pressure and other triggers.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
case materializeEagerly
```

#### Discussion

When a folder with the inherited policy is moved into a folder with this policy, the system will automatically schedule a download.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileprovidernamespacepolicy/materializeeagerly)*