# fileDialogURLEnabled(_:)

**Framework**: RealityKit  
**Kind**: method

On macOS, configures the the `fileImporter` or `fileMover` to conditionally disable presented URLs.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst ?+
- macOS 14.0+
- visionOS ?+

## Declaration

```swift
nonisolated
func fileDialogURLEnabled(_ predicate: Predicate<URL>) -> some View
```

## Parameters

- `predicate`: The predicate that evaluates the   URLs presented to the user to conditionally disable them.   The implementation is expected to have constant complexity   and should not access the files contents or metadata. A common use case   is inspecting the path or the file name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/realityviewdefaultplaceholder/filedialogurlenabled(_:))*