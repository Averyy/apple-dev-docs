# ManifestURL

**Framework**: Device Management  
**Kind**: dictionary

The URL to the app manifest.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- macOS 10.9+
- tvOS 10.2+
- visionOS 1.1+
- watchOS 10.0+

## Declaration

```swift
object ManifestURL
```

#### Discussion

Use SHA-256 hashes instead of MD5 because SHA-256 has stronger security. If both SHA-256 and MD5 hash properties are present, the device uses only the SHA-256 hashes to verify the manifest data.

## Topics

### Objects
- [object ManifestURL.ItemsItem](manifesturl/itemsitem.md)
  An array of dictionaries representing what the manifest installs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/manifesturl)*