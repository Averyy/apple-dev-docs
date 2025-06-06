# dropDestination(for:action:)

**Framework**: SwiftUI  
**Kind**: method

Sets the insert action for the dynamic table rows.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
func dropDestination<T>(for payloadType: T.Type = T.self, action: @escaping (Int, [T]) -> Void) -> ModifiedContent<Self, OnInsertTableRowModifier> where T : Transferable
```

#### Return Value

A view that calls `action` when elements are inserted into the original view.

#### Discussion

```swift
struct Profile: Identifiable {
    let givenName: String
    let familyName: String
    let id = UUID()
}

@State private var profiles: [Profile] = [
    Person(givenName: "Juan", familyName: "Chavez"),
    Person(givenName: "Mei", familyName: "Chen"),
    Person(givenName: "Tom", familyName: "Clark"),
    Person(givenName: "Gita", familyName: "Kumar")
]

var body: some View {
    Table {
        TableColumn("Given Name", value: \.givenName)
        TableColumn("Family Name", value: \.familyName)
    } rows: {
        ForEach(profiles) {
            TableRow($0)
        }
        .dropDestination(
            for: Profile.self
        ) { offset, receivedProfiles in
            people.insert(contentsOf: receivedProfiles, at: offset)
        }
    }
}
```

## Parameters

- `payloadType`: Type of the models that are dropped.
- `action`: A closure that SwiftUI invokes when elements are added to   the collection of rows.   The closure takes two arguments: The first argument is the   offset relative to the dynamic view’s underlying collection of data.   The second argument is an array of   items that   represents the data that you want to insert.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/dynamictablerowcontent/dropdestination(for:action:))*