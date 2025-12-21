# init(host:name:)

**Framework**: ExtensionFoundation  
**Kind**: init

Creates an identifier for binding to a host app’s extension point.

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
init(host bundleIdentifier: StaticString, name: StaticString)
```

## Parameters

- `name`: The name of the host app’s extension point. This name must match the value   in the   portion of an extension point definition.

## See Also

- [init(StaticString)](appextensionpoint/identifier/init(_:).md)
  Creates an identifier for binding to a system-defined extension point.


---

*[View on Apple Developer](https://developer.apple.com/documentation/extensionfoundation/appextensionpoint/identifier/init(host:name:))*