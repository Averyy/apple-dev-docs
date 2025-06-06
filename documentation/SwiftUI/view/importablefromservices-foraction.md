# importableFromServices(for:action:)

**Framework**: SwiftUI  
**Kind**: method

Enables importing items from services, such as Continuity Camera on macOS.

**Availability**:
- macOS 13.0+

## Declaration

```swift
nonisolated
func importableFromServices<T>(for payloadType: T.Type = T.self, action: @escaping ([T]) -> Bool) -> some View where T : Transferable
```

#### Discussion

```swift
@State private var title: String
var body: some View {
    Color.pink
        .frame(width: 400, height: 400)
        .importableFromServices(for: String.self) { titles
            title = titles.first ?? title
            return !titles.isEmpty
        }
}
```

## Parameters

- `payloadType`: The expected type of the imported models.
- `action`: A closure that will be called with the imported service   item. Return   to indicate that there was a failure to receive   the items.

## See Also

- [func exportableToServices<T>(@autoclosure () -> [T]) -> some View](view/exportabletoservices(_:).md)
  Exports items for consumption by shortcuts, quick actions, and services.
- [func exportableToServices<T>(@autoclosure () -> [T], onEdit: ([T]) -> Bool) -> some View](view/exportabletoservices(_:onedit:).md)
  Exports read-write items for consumption by shortcuts, quick actions, and services.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/importablefromservices(for:action:))*