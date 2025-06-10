# purchase

**Framework**: SwiftUI  
**Kind**: property

An action that starts an in-app purchase.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
@MainActor
@preconcurrency var purchase: PurchaseAction { get }
```

#### Discussion

Read this environment value to get an `PurchaseAction` instance for a given [`Environment`](environment.md). Call the instance to start an in-app purchase. You call the instance directly because it defines a `PurchaseAction/callAsFunction(_:options:)` method that Swift calls when you call the instance.

For example, you can start an in-app purchase when the user taps a button:

```swift
struct PurchaseExample: View {
    @Environment(\.purchase) private var purchase
    let product: Product
    let purchaseOptions: [Product.PurchaseOption]

    var body: some View {
        Button {
            Task {
                let purchaseResult = try? await purchase(product, options: purchaseOptions)
                // Process purchase result.
            }
        } label: {
            Text(product.displayName)
        }
    }
}
```

## See Also

- [var dismiss: DismissAction](environmentvalues/dismiss.md)
  An action that dismisses the current presentation.
- [var dismissSearch: DismissSearchAction](environmentvalues/dismisssearch.md)
  An action that ends the current search interaction.
- [var dismissWindow: DismissWindowAction](environmentvalues/dismisswindow.md)
  A window dismissal action stored in a view’s environment.
- [var openImmersiveSpace: OpenImmersiveSpaceAction](environmentvalues/openimmersivespace.md)
  An action that presents an immersive space.
- [var dismissImmersiveSpace: DismissImmersiveSpaceAction](environmentvalues/dismissimmersivespace.md)
  An immersive space dismissal action stored in a view’s environment.
- [var newDocument: NewDocumentAction](environmentvalues/newdocument.md)
  An action in the environment that presents a new document.
- [var openDocument: OpenDocumentAction](environmentvalues/opendocument.md)
  An action in the environment that presents an existing document.
- [var openURL: OpenURLAction](environmentvalues/openurl.md)
  An action that opens a URL.
- [var openWindow: OpenWindowAction](environmentvalues/openwindow.md)
  A window presentation action stored in a view’s environment.
- [var pushWindow: PushWindowAction](environmentvalues/pushwindow.md)
  A window presentation action stored in a view’s environment.
- [var refresh: RefreshAction?](environmentvalues/refresh.md)
  A refresh action stored in a view’s environment.
- [var rename: RenameAction?](environmentvalues/rename.md)
  An action that activates the standard rename interaction.
- [var resetFocus: ResetFocusAction](environmentvalues/resetfocus.md)
  An action that requests the focus system to reevaluate default focus.
- [var openSettings: OpenSettingsAction](environmentvalues/opensettings.md)
  A Settings presentation action stored in a view’s environment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/environmentvalues/purchase)*