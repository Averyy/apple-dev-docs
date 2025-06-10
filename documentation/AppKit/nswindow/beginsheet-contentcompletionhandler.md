# beginSheet(content:completionHandler:)

**Framework**: AppKit  
**Kind**: method

Presents a SwiftUI View as a sheet on the receiving NSWindow.

**Availability**:
- macOS 26.0+ (Beta)

## Declaration

```swift
@discardableResult
@MainActor @preconcurrency func beginSheet<V>(@ViewBuilder content: () -> V, completionHandler: (() -> Void)? = nil) -> NSWindow.HostingSheetRepresentation<V> where V : View
```

#### Return Value

A discardable `HostingSheetRepresentation` instance.

#### Discussion

The presented view supports the same features as when used in the `View.sheet(_:)` modifier, such as:

- Automatic dismissal with escape and `interactiveDismissDisabled()`
- Use of `@Environment(\.dismiss)` to dismiss the sheet
- Sheet sizing using `PresentationSizing`
- Standard sheet toolbars using `View.toolbar()`. parentWindow.beginSheet { NameADogSheet(dog: observableDog) } struct NameADogSheet: View { var dog: Dog @Environment(.dismiss) private var dismiss @State private var name: String = “” ```None
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
``` }

The returned `HostingSheetRepresentation` can be ignored unless the sheet needs to be manipulated from an AppKit context, such as changing the root view or programmatically changing the sheet.

## Parameters

- `content`: The SwiftUI view to present in a sheet.
- `completionHandler`: An optional completion handler that is called   when the sheet is dismissed for any reason.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/beginsheet(content:completionhandler:))*