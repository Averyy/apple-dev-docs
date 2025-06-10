# requestExport(for:)

**Framework**: Authentication Services  
**Kind**: method

Call this method to begin the export process. This will bring up the out of process system UI that will guide the user through the rest of the export flow. Once the necessary options have been determined, they will be returned here. After receiving the export options, call `exportCredentials(_:)` with the exported credentials in the specified format.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
func requestExport(for extensionBundleIdentifier: String? = nil) async throws -> ASCredentialExportManager.ExportOptions
```

#### Return Value

The selected set of export options.

## Parameters

- `extensionBundleIdentifier`: If your application contains more than one credential provider   extension, pass the bundle identifier of the extension doing the export here. If your application contains exactly one   credential provider extension, you may pass nil to indicate you are exporting on behalf of that extension. It is an   error to pass nil if your application contains more than one credential provider extension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/ascredentialexportmanager/requestexport(for:))*