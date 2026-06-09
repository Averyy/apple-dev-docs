# confirmationDialog(_:item:titleVisibility:actions:)

**Framework**: SwiftUI  
**Kind**: method

Presents a confirmation dialog using data to produce the dialog’s content and a text view for the title.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
nonisolated
func confirmationDialog<A, T>(_ title: Text, item data: Binding<T?>, titleVisibility: Visibility = .automatic, @ContentBuilder actions: (T) -> A) -> some View where A : View
```

## Parameters

- `title`: The title of the dialog.
- `data`: A binding to optional source of truth for the confirmation dialog. The system presents the dialog when the binding’s value is non-nil. When the user presses or taps the dialog’s default action button, the system sets this value to `nil` and dismisses. The system passes the contents to the modifier’s closures. You use this data to populate the fields of a confirmation dialog that you create that the system displays to the user.
- `titleVisibility`: The visibility of the dialog’s title. The default value is [`Visibility.automatic`](visibility/automatic.md).
- `actions`: A [`ContentBuilder`](contentbuilder.md) returning the dialog’s actions given the currently available data.

## See Also

- [func confirmationDialog(_:isPresented:titleVisibility:actions:)](view/confirmationdialog(_:ispresented:titlevisibility:actions:).md)
  Presents a confirmation dialog when a given condition is true, using a text view for the title.
- [func confirmationDialog(_:isPresented:titleVisibility:presenting:actions:)](view/confirmationdialog(_:ispresented:titlevisibility:presenting:actions:).md)
  Presents a confirmation dialog using data to produce the dialog’s content and a text view for the title.
- [func dismissalConfirmationDialog(_:shouldPresent:actions:)](view/dismissalconfirmationdialog(_:shouldpresent:actions:).md)
  Presents a confirmation dialog when a dismiss action has been triggered.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/confirmationdialog(_:item:titlevisibility:actions:))*