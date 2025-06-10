# buildBlock(_:_:)

**Framework**: ExtensionFoundation  
**Kind**: method

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 1.1+
- watchOS 26.0+ (Beta)

## Declaration

```swift
static func buildBlock<each T>(_ name: AppExtensionPoint.Name, _ attributes: repeat each T) -> AppExtensionPoint where repeat each T : AppExtensionPoint.Attribute
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/extensionfoundation/appextensionpoint/definition/buildblock(_:_:))*