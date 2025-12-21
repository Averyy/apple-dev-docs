# init(identifier:)

**Framework**: ExtensionFoundation  
**Kind**: init

Initializes the type with a string you can use to find the extension point.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 1.1+
- watchOS 26.0+

## Declaration

```swift
init(identifier: StaticString) throws
```

#### Discussion

- Paramerters: - identifier: The name of the extension point. This string isn’t the same as the value you put in the [`AppExtensionPoint.Identifier`](appextensionpoint/identifier.md) type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/extensionfoundation/appextensionpoint/init(identifier:))*