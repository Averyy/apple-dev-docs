# documentConfiguration

**Framework**: SwiftUI  
**Kind**: property

The configuration of a document in a [`DocumentGroup`](documentgroup.md).

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 1.0+

## Declaration

```swift
var documentConfiguration: DocumentConfiguration? { get }
```

#### Discussion

The value is `nil` for views that are not enclosed in a [`DocumentGroup`](documentgroup.md).

For example, if the app shows the document path in the footer of each document, it can get the URL from the environment:

```swift
struct ContentView: View {
    @Binding var document: TextDocument
    @Environment(\.documentConfiguration) private var configuration: DocumentConfiguration?

    var body: some View {
        …
        Label(
            configuration?.fileURL?.path ??
                "", systemImage: "folder.circle"
        )
    }
}
```

## See Also

- [struct DocumentConfiguration](documentconfiguration.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/environmentvalues/documentconfiguration)*