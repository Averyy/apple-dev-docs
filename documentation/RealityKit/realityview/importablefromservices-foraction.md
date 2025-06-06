# importableFromServices(for:action:)

**Framework**: RealityKit  
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

```None
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/realityview/importablefromservices(for:action:))*