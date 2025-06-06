# fileDialogImportsUnresolvedAliases(_:)

**Framework**: DeviceActivity  
**Kind**: method

On macOS, configures the `fileExporter`, `fileImporter`, or `fileMover` behavior when a user chooses an alias.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+

## Declaration

```swift
nonisolated
func fileDialogImportsUnresolvedAliases(_ imports: Bool) -> some View
```

#### Discussion

By default, file dialogs resolve aliases and provide the URL of the item referred to by the chosen alias. This modifier allows control of this behavior: pass `true` if the application doesn’t want file dialog to resolve aliases.

## Parameters

- `imports`: A Boolean value that indicates   if the application receives unresolved or resolved URLs   when a user chooses aliases.


---

*[View on Apple Developer](https://developer.apple.com/documentation/deviceactivity/deviceactivityreport/filedialogimportsunresolvedaliases(_:))*