# body

**Framework**: ExtensionKit  
**Kind**: property  
**Required**: Yes

The content and behavior of the scene’s interface.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
@MainActor
@preconcurrency var body: Self.Body { get }
```

#### Discussion

For the body of your scene, specify a [`PrimitiveAppExtensionScene`](primitiveappextensionscene.md) structure with the contents you want to display. You can also use that structure to configure an XPC connection for handling any interface-related data exchanges.

## See Also

- [associatedtype Body : AppExtensionScene](appextensionscene/body-swift.associatedtype.md)
  The type for this scene’s body.


---

*[View on Apple Developer](https://developer.apple.com/documentation/extensionkit/appextensionscene/body-swift.property)*