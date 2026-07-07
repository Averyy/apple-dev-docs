# credentialDataManager

**Framework**: SwiftUI  
**Kind**: property

This environment variable is for SwiftUI clients of the ASCredentialDataManager API. An example usage might look like:

**Availability**:
- iOS 26.2+
- iPadOS 26.2+
- macOS 26.2+
- visionOS 26.2+

## Declaration

```swift
var credentialDataManager: CredentialDataManager { get }
```

#### Discussion

```swift
struct CredentialDataManagerExample: View {
    @Environment(\.credentialDataManager) private var credentialDataManager

    var body: some View {
        Button("Save Credentials") {
            Task {
                do {
                    let credential = getCredential() // defined elsewhere
                    let scope = getScope()
                    try await credentialDataManager.save(credential: credential, for: scope)
                } catch {
                    // code to handle the save error
                }
            }
        }
    }
}
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/environmentvalues/credentialdatamanager)*