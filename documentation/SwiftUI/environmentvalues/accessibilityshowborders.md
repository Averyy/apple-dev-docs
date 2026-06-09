# accessibilityShowBorders

**Framework**: SwiftUI  
**Kind**: property

Whether the system preference for Show Borders is enabled.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
@backDeployed(before: iOS 26.1, macOS 26.1, tvOS 26.1, watchOS 26.1, visionOS 26.1)
var accessibilityShowBorders: Bool { get }
```

#### Discussion

On macOS 27 and later, the system provides a dedicated Show Borders setting in System Settings. On earlier versions of macOS, this value is true when Increased Contrast is enabled.

When this value is true, draw interactive custom controls such as buttons with clearly visible edges so they remain distinguishable at any window size:

```swift
struct BorderedButton: View {
    @Environment(\.accessibilityShowBorders) var showBorders

    var body: some View {
        Label("Archive", systemImage: "archivebox")
            .padding(8)
            .overlay {
                if showBorders {
                    RoundedRectangle(cornerRadius: 8)
                        .stroke(.secondary)
                }
            }
    }
}
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/environmentvalues/accessibilityshowborders)*