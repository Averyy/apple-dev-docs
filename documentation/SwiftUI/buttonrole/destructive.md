# destructive

**Framework**: SwiftUI  
**Kind**: property  
**Role**: Type Property

A role that indicates a destructive button.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
static let destructive: ButtonRole
```

## Mentions

- [Populating SwiftUI menus with adaptive controls](../populating-swiftui-menus-with-adaptive-controls.md)

#### Discussion

Use this role for a button that deletes user data, or performs an irreversible operation. A destructive button signals by its appearance that the user should carefully consider whether to tap or click the button. For example, SwiftUI presents a destructive button that you add with the [`swipeActions(edge:allowsFullSwipe:content:)`](../view/swipeactions%28edge,allowsfullswipe,content%29.md) modifier using a red background:

```swift
List {
    ForEach(items) { item in
        Text(item.title)
            .swipeActions {
                Button(role: .destructive) { delete() } label: {
                    Label("Delete", systemImage: "trash")
                }
            }
    }
}
.navigationTitle("Shopping List")
```

![A screenshot of a list of three items, where the second item is](https://developer.apple.com/tutorials/images/com.apple.SwiftUI/ButtonRole-destructive-1@2x.png)

## See Also

### Getting button roles
- [static let cancel: ButtonRole](./cancel.md)
  A role that indicates a button that cancels an operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/buttonrole/destructive)*