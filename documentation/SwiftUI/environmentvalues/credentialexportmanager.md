# credentialExportManager

**Framework**: SwiftUI  
**Kind**: property

This environment variable is for SwiftUI clients of the credential exchange API. An example usage might look like:

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
var credentialExportManager: ASCredentialExportManager { get }
```

#### Discussion

```swift
struct CredentialExchangeManagerExample: View {
    @Environment(\.credentialExchangeManager) private var credentialExchangeManager

    var body: some View {
        Button("Export Credentials") {
            Task {
                do {
                    let credentialData = getCredentialData() // defined elsewhere
                    try await credentialExchangeManager.exportCredentials(credentialData)
                } catch {
                    // code to handle the export error
                }
            }
        }
    }
}
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/environmentvalues/credentialexportmanager)*