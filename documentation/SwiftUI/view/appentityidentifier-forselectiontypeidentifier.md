# appEntityIdentifier(forSelectionType:identifier:)

**Framework**: SwiftUI  
**Kind**: method

Associates the items in a SwiftUI list view with app entities to make them discoverable by Apple Intelligence and Siri.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- macOS 15.4+
- tvOS 18.4+
- visionOS 2.4+
- watchOS 11.4+

## Declaration

```swift
nonisolated
func appEntityIdentifier<I>(forSelectionType itemType: I.Type = I.self, identifier: @escaping @Sendable (I) -> EntityIdentifier?) -> some View where I : Hashable
```

#### Discussion

Use this modifier to make app entities that describe data in a list discoverable by Apple Intelligence and Siri. This provides additional context to the system when the list appears onscreen and people scroll through it.

The following example associates a [`List`](List.md) view that displays books with an app entity for each book in the list.

```swift
struct BookListView: View {
   let books: [Book]
   @State private var selection = Set<Book.ID>()
   var body: some View {
       List(selection: $selection) {
           ForEach(books) { book in
               BookView(book.name)
           }
       }
       .appEntityIdentifier(forSelectionType: Book.ID.self) { bookId in
           EntityIdentifier(for: Book.self, identifier: bookId)
       }
   }
 }
```

For more information, refer to doc:providing-contextual-cues-to-Apple-Intelligence-and-Siri and [`App Intents`](https://developer.apple.com/documentation/AppIntents).

## See Also

- [func appEntityIdentifier(EntityIdentifier?) -> some View](view/appentityidentifier(_:).md)
  Associates a SwiftUI view with an app entity to make its content discoverable by Apple Intelligence and Siri.
- [func appEntityUIElements((AppEntityUIElementsContext) -> [AppEntityUIElement]) -> some View](view/appentityuielements(_:).md)
  Provides the system with additional context to make a custom view’s content discoverable by Apple Intelligence and Siri.
- [func onAppIntentExecution<I>(I.Type, perform: (I) -> Void) -> some View](view/onappintentexecution(_:perform:).md)
  Registers a handler to invoke in response to the specified app intent that your app receives.
- [func shortcutsLinkStyle(ShortcutsLinkStyle) -> some View](view/shortcutslinkstyle(_:).md)
  Sets the given style for ShortcutsLinks within the view hierarchy
- [func siriTipViewStyle(SiriTipViewStyle) -> some View](view/siritipviewstyle(_:).md)
  Sets the given style for SiriTipView within the view hierarchy


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/appentityidentifier(forselectiontype:identifier:))*