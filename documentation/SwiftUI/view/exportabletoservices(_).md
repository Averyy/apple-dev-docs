# exportableToServices(_:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Exports items for consumption by shortcuts, quick actions, and services.

**Availability**:
- macOS 13.0+

## Declaration

```swift
nonisolated
func exportableToServices<T>(_ payload: @autoclosure @escaping () -> [T]) -> some View where T : Transferable
```

#### Discussion

If the associated view supports selection, the exported item should reflect that selected subpart.

```swift
var title: String
var body: some View {
    Color.pink
        .frame(width: 400, height: 400)
        .exportableToServices([title])
}
```

## Parameters

- `payload`: A closure that will be called on request of the items by the shortcut or service.

## See Also

### Importing and exporting transferable items
- [func importableFromServices<T>(for: T.Type, action: ([T]) -> Bool) -> some View](./importablefromservices%28for,action%29.md)
  Enables importing items from services, such as Continuity Camera on macOS.
- [func exportableToServices<T>(@autoclosure () -> [T], onEdit: ([T]) -> Bool) -> some View](./exportabletoservices%28_,onedit%29.md)
  Exports read-write items for consumption by shortcuts, quick actions, and services.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/exportabletoservices(_:))*