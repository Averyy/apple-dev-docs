# beginSheet(content:completionHandler:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Presents a SwiftUI view as a sheet on the receiving NSWindow.

**Availability**:
- macOS 26.0+

## Declaration

```swift
@discardableResult
@MainActor @preconcurrency func beginSheet<V>(@ContentBuilder content: () -> V, completionHandler: (() -> Void)? = nil) -> NSWindow.HostingSheetRepresentation<V> where V : View
```

## Return Value

A discardable [`NSWindow.HostingSheetRepresentation`](./hostingsheetrepresentation.md) instance.

## Discussion

The presented view supports the same features as when used in the [`sheet(isPresented:onDismiss:content:)`](../../SwiftUI/view/sheet%28ispresented,ondismiss,content%29.md) or [`sheet(item:onDismiss:content:)`](../../SwiftUI/view/sheet%28item,ondismiss,content%29.md) view modifier, such as:

- Automatic dismissal with the Escape key and disabling interactive dismissal with [`interactiveDismissDisabled(_:)`](../../SwiftUI/view/interactivedismissdisabled%28_%29.md)
- Use of [`@Environment(\.dismiss)`](../../SwiftUI/environmentvalues/dismiss.md) to dismiss the sheet
- Sheet sizing using [`presentationSizing(_:)`](../../SwiftUI/view/presentationsizing%28_%29.md)
- Standard sheet toolbars using [`toolbar(content:)`](../../SwiftUI/view/toolbar%28content%29.md).

```
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

The returned [`NSWindow.HostingSheetRepresentation`](./hostingsheetrepresentation.md) can be ignored unless the sheet needs to be manipulated from an AppKit context, such as changing the root view or programmatically changing the sheet.

## Parameters

- `content`: The SwiftUI view to present in a sheet.
- `completionHandler`: An optional completion handler that is called when the sheet is dismissed for any reason.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/beginsheet(content:completionhandler:))*