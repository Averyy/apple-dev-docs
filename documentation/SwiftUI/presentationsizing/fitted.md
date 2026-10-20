# fitted

**Framework**: SwiftUI  
**Kind**: property  
**Role**: Type Property

The presentation sizing is dictated by the ideal size of the content

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
static var fitted: FittedPresentationSizing { get }
```

Available when `Self` is `FittedPresentationSizing`.

#### Discussion

On macOS, presentations with `.fitted` sizing are user-resizable by default. Because of this, is best practice to define a presentation frame with any of the `frame` modifiers, either specifying a fixed frame or minimum/maximum bounds. If you specify a [`fixedSize()`](../view/fixedsize%28%29.md) or a frame with fixed dimensions on the content, the sheet will not be user resizable.

```swift
@State private var present = true

ContentView().sheet(isPresented: $present) {
  ScrollView {
    LazyVGrid(columns: columns) {
      ForEach(0x1f600...0x1f679, id: \.self) { value in
        Text(String(format: "%x", value))
        Text(emoji(value))
          .font(.largeTitle)
        }
      }
  }
  .presentationSizing(.fitted)
  .frame(
    minWidth: 200, idealWidth: 300, maxWidth: 500,
    minHeight: 100, maxHeight: 600)
}
```

To create a view that fits the view’s size in either the horizontal or vertical dimensions, see [`fitted(horizontal:vertical:)`](./fitted%28horizontal,vertical%29.md).

## See Also

### Getting built-in presentation size
- [static var automatic: AutomaticPresentationSizing](./automatic.md)
  The default presentation sizing, appropriate for the platform.
- [static var form: FormPresentationSizing](./form.md)
  The size is appropriate for forms and slightly less wide than`.page`
- [static var page: PagePresentationSizing](./page.md)
  The size is roughly the size of a page of paper, appropriate for informational or compositional content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/presentationsizing/fitted)*