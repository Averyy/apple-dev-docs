# init(version:info:retain:release:copyDescription:)

**Framework**: System Configuration  
**Kind**: init

Creates a preferences context with the specified raw values.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
init(version: CFIndex, info: UnsafeMutableRawPointer?, retain: ((UnsafeRawPointer) -> UnsafeRawPointer)?, release: ((UnsafeRawPointer) -> Void)?, copyDescription: ((UnsafeRawPointer) -> Unmanaged<CFString>)?)
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/systemconfiguration/scpreferencescontext/init(version:info:retain:release:copydescription:))*