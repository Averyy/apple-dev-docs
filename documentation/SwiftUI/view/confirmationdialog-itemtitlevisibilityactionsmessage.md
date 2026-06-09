# confirmationDialog(_:item:titleVisibility:actions:message:)

**Framework**: SwiftUI  
**Kind**: method

Presents a confirmation dialog with a message using data to produce the dialog’s content and a text view for the message.

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
func confirmationDialog<A, M, T>(_ title: Text, item data: Binding<T?>, titleVisibility: Visibility = .automatic, @ContentBuilder actions: (T) -> A, @ContentBuilder message: (T) -> M) -> some View where A : View, M : View
```

## Parameters

- `title`: The title of the dialog.
- `data`: A binding to optional source of truth for the confirmation dialog. The system presents the dialog when the binding’s value is non-nil. When the user presses or taps the dialog’s default action button, the system sets this value to `nil` and dismisses. The system passes the contents to the modifier’s closures. You use this data to populate the fields of a confirmation dialog that you create that the system displays to the user.
- `titleVisibility`: The visibility of the dialog’s title. The default value is [`Visibility.automatic`](visibility/automatic.md).
- `actions`: A [`ContentBuilder`](contentbuilder.md) returning the dialog’s actions given the currently available data.
- `message`: A [`ContentBuilder`](contentbuilder.md) returning the message for the dialog given the currently available data.

## See Also

- [func confirmationDialog(_:isPresented:titleVisibility:actions:message:)](view/confirmationdialog(_:ispresented:titlevisibility:actions:message:).md)
  Presents a confirmation dialog with a message when a given condition is true, using a text view for the title.
- [func confirmationDialog(_:isPresented:titleVisibility:presenting:actions:message:)](view/confirmationdialog(_:ispresented:titlevisibility:presenting:actions:message:).md)
  Presents a confirmation dialog with a message using data to produce the dialog’s content and a text view for the message.
- [func dismissalConfirmationDialog(_:shouldPresent:actions:message:)](view/dismissalconfirmationdialog(_:shouldpresent:actions:message:).md)
  Presents a confirmation dialog when a dismiss action has been triggered.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/confirmationdialog(_:item:titlevisibility:actions:message:))*