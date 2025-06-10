# dropDestination(for:isEnabled:action:)

**Framework**: FinanceKitUI  
**Kind**: method

Defines the destination of a drag and drop operation that provides a drop operation proposal and handles the dropped content with a closure that you specify.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
nonisolated
func dropDestination<T>(for type: T.Type = T.self, isEnabled: Bool = true, action: @escaping ([T], DropSession) -> Void) -> some View where T : Transferable
```

#### Return Value

A view that provides a drop destination for a drop operation of the specified type.

#### Discussion

The dropped content can be provided as binary data, file URLs, or file promises.

The drop destination is the same size and position as this view.

```None
@State private var isDropTargeted = false
@Binding var isDropEnabled: Bool

var body: some View {
    Color.pink
        .frame(width: 400, height: 400)
        .dropDestination(
            for: String.self, isEnabled: isDropEnabled
        ) { receivedTitles, session in
            animateDrop(at: session.location)
            process(titles: receivedTitles)
        }
}

func process(titles: [String]) { ... }
func animateDrop(at: CGPoint) { ... }
```

## Parameters

- `type`: The expected type of the dropped models.
- `isEnabled`: The Boolean value indicating if the view accepts drop interactions.
- `action`: A closure that takes the dropped content and responds   appropriately. The first parameter to   contains   the dropped items. The second parameter contains the drop session description.


---

*[View on Apple Developer](https://developer.apple.com/documentation/financekitui/transactionpicker/dropdestination(for:isenabled:action:))*