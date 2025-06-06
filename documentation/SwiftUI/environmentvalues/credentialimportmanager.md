# credentialImportManager

**Framework**: SwiftUI  
**Kind**: property

This environment variable is for SwiftUI clients of the credential exchange API. An example usage might look like:

**Availability**:
- iOS 18.2+
- iPadOS 18.2+
- macOS 15.2+
- visionOS 2.2+

## Declaration

```swift
var credentialImportManager: ASCredentialImportManager { get }
```

#### Discussion

```swift
struct CredentialImportManagerExample: View {
    @Environment(\.credentialImportManager) private var credentialImportManager

    var body: some View {
        content // defined elsewhere
            .onContinueUserActivity(ASCredentialExchangeActivityType) { activity in
                Task {
                    do {
                        guard let token = activity.userInfo?[ASCredentialImportToken] as? UUID else { return }
                        let credentialData = try await credentialImportManager.importCredentials(token: token)
                        // do something with the data
                    } catch {
                        // code to handle the import error
                    }
                }
            }
    }
}
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/environmentvalues/credentialimportmanager)*