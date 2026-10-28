# Configuration

**Framework**: ExtensionFoundation  
**Kind**: associatedtype  
**Role**: Associated Type  
**Required**: Yes

A type that manages configuration data for an app extension.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.1+
- watchOS 9.0+

## Declaration

```swift
associatedtype Configuration : AppExtensionConfiguration
```

## Discussion

When you create a custom app extension, Swift infers this type from your implementation of the required [`configuration`](./configuration-swift.property.md) property.

## See Also

### Configuring the app extension
- [var configuration: Self.Configuration](./configuration-swift.property.md)
  The configuration details for this app extension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/extensionfoundation/appextension/configuration-swift.associatedtype)*