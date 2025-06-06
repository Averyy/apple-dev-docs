# exportableToServices(_:onEdit:)

**Framework**: SwiftUI  
**Kind**: method

Exports read-write items for consumption by shortcuts, quick actions, and services.

**Availability**:
- macOS 13.0+

## Declaration

```swift
nonisolated
func exportableToServices<T>(_ payload: @autoclosure @escaping () -> [T], onEdit: @escaping ([T]) -> Bool) -> some View where T : Transferable
```

#### Discussion

If the associated view supports selection, the exported item should reflect that selected subpart.

```swift
@State private var title: String
var body: some View {
    Color.pink
        .frame(width: 400, height: 400)
        .exportableToServices([title]) { editedTitles
            title = editedTitles.first ?? title
            return !editedTitles.isEmpty
        }
}
```

## Parameters

- `payload`: A closure that will be called on request of the items   by the shortcut or service.
- `onEdit`: A closure that will be called after the shortcut or   service completes with its output data. This should replace the   selected subpart that was exported with  . Return   to   indicate that there was a failure to receive the items.

## See Also

- [func importableFromServices<T>(for: T.Type, action: ([T]) -> Bool) -> some View](view/importablefromservices(for:action:).md)
  Enables importing items from services, such as Continuity Camera on macOS.
- [func exportableToServices<T>(@autoclosure () -> [T]) -> some View](view/exportabletoservices(_:).md)
  Exports items for consumption by shortcuts, quick actions, and services.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/exportabletoservices(_:onedit:))*