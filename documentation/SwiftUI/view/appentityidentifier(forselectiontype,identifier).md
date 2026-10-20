# appEntityIdentifier(forSelectionType:identifier:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Associates the items in a SwiftUI list view with app entities to make them discoverable by Apple Intelligence and Siri.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
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

The following example associates a [`List`](../list.md) view that displays books with an app entity for each book in the list.

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

For more information, refer to [Providing contextual cues to Apple Intelligence and Siri](../../AppIntents/providing-contextual-cues-to-apple-intelligence-and-siri.md) and [App Intents](../../AppIntents/AppIntents.md).

## See Also

### App intents
- [func appEntityIdentifier(EntityIdentifier?) -> some View](./appentityidentifier%28_%29.md)
  Associates a SwiftUI view with an app entity to make its content discoverable by Apple Intelligence and Siri.
- [func appEntityUIElements((AppEntityUIElementsContext) -> [AppEntityUIElement]) -> some View](./appentityuielements%28_%29.md)
  Provides the system with additional context to make a custom view’s content discoverable by Apple Intelligence and Siri.
- [func onAppIntentExecution<I>(I.Type, perform: (I) -> Void) -> some View](./onappintentexecution%28_,perform%29.md)
  Registers a handler to run when the app receives an app intent that targets the associated scene.
- [func shortcutsLinkStyle(ShortcutsLinkStyle) -> some View](./shortcutslinkstyle%28_%29.md)
  Sets the given style for ShortcutsLinks within the view hierarchy
- [func siriTipViewStyle(SiriTipViewStyle) -> some View](./siritipviewstyle%28_%29.md)
  Sets the given style for SiriTipView within the view hierarchy


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/appentityidentifier(forselectiontype:identifier:))*