# SecExternalFormat.formatUnknown

**Framework**: Security  
**Kind**: case

**Availability**:
- macOS 10.0+

## Declaration

```swift
case formatUnknown
```

#### Discussion

When importing, indicates the format is unknown. When exporting, use the default format for the item. For asymmetric keys, the default is `kSecFormatOpenSSL`. For symmetric keys, the default is `kSecFormatRawKey`. For certificates, the default is `kSecFormatX509Cert`. For multiple items, the default is `kSecFormatPEMSequence`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/secexternalformat/formatunknown)*