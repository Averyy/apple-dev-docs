# openSettings(for:)

**Framework**: Accessibility  
**Kind**: method

Opens the Settings app to a specific section of Accessibility settings.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
static func openSettings(for feature: AccessibilitySettings.Feature) async throws
```

#### Discussion

Some app behaviors depend on a person turning on a specific Accessibility setting on their device. You can use this method to open the Settings app to a specific Accessibility setting to help people turn it on more quickly, as shown in the following code example.

```swift
ContentView()
    .alert(
        "Use Personal Voice",
        isPresented: $showAlert
    ) {
        Button("Open Accessibility Settings") {
            Task {
                do {
                    try await AccessibilitySettings.openSettings(for: .personalVoiceAllowAppsToRequestToUse)
                } catch {
                    print("Error: \(error)")
                }
            }
        }
        Button("Cancel", role: .cancel) { }
    } message: {
        Text("To use this feature, turn on the Personal Voice > Allow Apps to Request to Use setting.")
    }
```

## See Also

- [AccessibilitySettings.Feature](accessibilitysettings/feature.md)
  Constants that describe specific Accessibility settings in the Settings app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessibility/accessibilitysettings/opensettings(for:))*