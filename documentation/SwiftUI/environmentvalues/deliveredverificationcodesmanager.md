# deliveredVerificationCodesManager

**Framework**: SwiftUI  
**Kind**: property

This environment variable is for SwiftUI clients of the ASDeliveredVerificationCodesManager API. An example usage might look like:

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
var deliveredVerificationCodesManager: DeliveredVerificationCodesManager { get }
```

#### Discussion

```swift
struct DeliveredVerificationCodesManagerExample: View {
    @Environment(\.deliveredVerificationCodesManager) private var deliveredVerificationCodesManager

    let preferredDuration: TimeInterval

    var body: some View {
        Button("Listen for Codes") {
            Task {
                do {
                    let codes = try deliveredVerificationCodesManager.oneTimeCodes(preferredDuration: preferredDuration)
                    for try await code in codes {
                        handle(code: code)
                    }
                } catch DeliveredVerificationCodesManager.VerificationError.userPermissionDenied {
                    // Explaining why OTCs are needed or try without codes
                } catch DeliveredVerificationCodesManager.VerificationError.appIsNotEnabledCredentialProvider {
                    // Show UI explaining how to turn on the app as a Password Manager
                } catch {
                    // code to handle the save error
                }
            }
        }
    }
}
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/environmentvalues/deliveredverificationcodesmanager)*