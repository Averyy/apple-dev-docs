# init(systemName:)

**Framework**: SwiftUI  
**Kind**: init

Creates a system symbol image.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 11.0+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
init(systemName: String)
```

#### Discussion

This initializer creates an image using a system-provided symbol. Use [`SF Symbols`](https://developer.apple.comhttps://developer.apple.com/design/resources/#sf-symbols) to find symbols and their corresponding names.

To create a custom symbol image from your app’s asset catalog, use [`init(_:bundle:)`](image/init(_:bundle:).md) instead.

## Parameters

- `systemName`: The name of the system symbol image.   Use the SF Symbols app to look up the names of system symbol images.

## See Also

- [init(systemName: String, variableValue: Double?)](image/init(systemname:variablevalue:).md)
  Creates a system symbol image with a variable value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/image/init(systemname:))*