# dropDestination(for:action:)

**Framework**: SwiftUI  
**Kind**: method

Sets the insert action for the dynamic view.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
nonisolated
func dropDestination<T>(for payloadType: T.Type = T.self, action: @escaping ([T], Int) -> Void) -> some DynamicViewContent where T : Transferable
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
    List {
        ForEach(profiles) { profile in
            Text(profile.givenName)
        }
        .dropDestination(for: Profile.self) { receivedProfiles, offset in
            profiles.insert(contentsOf: receivedProfiles, at: offset)
        }
    }
}
```

## Parameters

- `payloadType`: Type of the models that are dropped.
- `action`: A closure that SwiftUI invokes when elements are added to   the view. The closure takes two arguments: The first argument is the   offset relative to the dynamic view’s underlying collection of data.   The second argument is an array of   items that   represents the data that you want to insert.

## See Also

- [func onDelete(perform: Optional<(IndexSet) -> Void>) -> some DynamicViewContent](dynamicviewcontent/ondelete(perform:).md)
  Sets the deletion action for the dynamic view. You must delete the corresponding item within `action`, as it will be called after the row has already been removed from the [`List`](list.md).
- [func onInsert(of: [UTType], perform: (Int, [NSItemProvider]) -> Void) -> some DynamicViewContent](dynamicviewcontent/oninsert(of:perform:)-418bq.md)
  Sets the insert action for the dynamic view.
- [func onMove(perform: Optional<(IndexSet, Int) -> Void>) -> some DynamicViewContent](dynamicviewcontent/onmove(perform:).md)
  Sets the move action for the dynamic view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/dynamicviewcontent/dropdestination(for:action:))*