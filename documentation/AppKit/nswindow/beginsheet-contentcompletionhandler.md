# beginSheet(content:completionHandler:)

**Framework**: AppKit  
**Kind**: method

Presents a SwiftUI view as a sheet on the receiving NSWindow.

**Availability**:
- macOS 26.0+

## Declaration

```swift
@discardableResult
@MainActor @preconcurrency func beginSheet<V>(@ContentBuilder content: () -> V, completionHandler: (() -> Void)? = nil) -> NSWindow.HostingSheetRepresentation<V> where V : View
```

#### Return Value

A discardable [`NSWindow.HostingSheetRepresentation`](nswindow/hostingsheetrepresentation.md) instance.

#### Discussion

The presented view supports the same features as when used in the [`sheet(isPresented:onDismiss:content:)`](https://developer.apple.com/documentation/SwiftUI/View/sheet(isPresented:onDismiss:content:)) or [`sheet(item:onDismiss:content:)`](https://developer.apple.com/documentation/SwiftUI/View/sheet(item:onDismiss:content:)) view modifier, such as:

- Automatic dismissal with the Escape key and disabling interactive dismissal with [`interactiveDismissDisabled(_:)`](https://developer.apple.com/documentation/SwiftUI/View/interactiveDismissDisabled(_:))
- Use of [`dismiss`](https://developer.apple.com/documentation/SwiftUI/EnvironmentValues/dismiss) to dismiss the sheet
- Sheet sizing using [`presentationSizing(_:)`](https://developer.apple.com/documentation/SwiftUI/View/presentationSizing(_:))
- Standard sheet toolbars using [`toolbar(content:)`](https://developer.apple.com/documentation/SwiftUI/View/toolbar(content:)).

```None
parentWindow.beginSheet {
    NameADogSheet(dog: observableDog)
}

struct NameADogSheet: View {
    var dog: Dog
    @Environment(\.dismiss) private var dismiss
    @State private var name: String = ""

    var body: some View {
        Form {
            TextField("Who's a good dog?", text: $name)
        }
        .formStyle(.grouped)
        .toolbar {
            ToolbarItem(placement: .cancellationAction) {
                Button("Cancel") {
                    dismiss()
                }
            }
            ToolbarItem(placement: .confirmationAction) {
                Button("Suggest Name") {
                    dog.name = name
                    dismiss()
                }
                .disabled(name.isEmpty)
            }
        }
    }
}
```

The returned [`NSWindow.HostingSheetRepresentation`](nswindow/hostingsheetrepresentation.md) can be ignored unless the sheet needs to be manipulated from an AppKit context, such as changing the root view or programmatically changing the sheet.

## Parameters

- `content`: The SwiftUI view to present in a sheet.
- `completionHandler`: An optional completion handler that is called when the sheet is dismissed for any reason.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/beginsheet(content:completionhandler:))*