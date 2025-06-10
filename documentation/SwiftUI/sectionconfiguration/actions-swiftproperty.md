# actions

**Framework**: SwiftUI  
**Kind**: property

Custom actions associated with a section.

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
var actions: SectionConfiguration.Actions { get }
```

#### Discussion

This property provides programmatic access to the actions defined on a [`Section`](section.md). If no actions were specified, the collection will be empty. The following `MailboxView` will put actions into an overflow menu if there are too many to display inline.

```swift
struct MailboxView<Content: View>: View {
    var content: Content

    init(@ViewBuilder content: () -> Content) {
        self.content = content()
    }

    var body: some View {
        ForEach(sections: content) { section in
            HStack {
                section.header
                Spacer()
                Group(subviews: section.actions) { actions in
                    if actions.count > 2 {
                        actions[0]
                        // Place the extras in an overflow menu.
                        Menu("Actions", systemImage: "plus") {
                            actions[1...]
                        }
                    } else {
                        actions
                    }
                }
            }
            section.content
        }
    }
}
```

You can then use actions in `MailboxView` without considering overflow.

```swift
MailboxView {
    Section("iCloud") {
        Label("Receipts", systemImage: "folder")
        Label("Mailing Lists", systemImage: "folder")
    }
    .sectionActions {
        Button("New", systemImage: "folder.badge.plus") {}
        Button("Edit", systemImage: "folder.badge.gearshape") {}
        Button("Delete", systemImage: "folder.badge.minus") {}
    }
}
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/sectionconfiguration/actions-swift.property)*