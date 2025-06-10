# dropDestination(for:action:isTargeted:)

**Framework**: App Intents  
**Kind**: method

Defines the destination of a drag and drop operation that handles the dropped content with a closure that you specify.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- macOS 13.0+
- visionOS ?+

## Declaration

```swift
nonisolated
func dropDestination<T>(for payloadType: T.Type = T.self, action: @escaping ([T], CGPoint) -> Bool, isTargeted: @escaping (Bool) -> Void = { _ in }) -> some View where T : Transferable
```

#### Return Value

A view that provides a drop destination for a drag operation of the specified type.

#### Discussion

The dropped content can be provided as binary data, file URLs, or file promises.

The drop destination is the same size and position as this view.

```swift
@State private var isDropTargeted = false

var body: some View {
    Color.pink
        .frame(width: 400, height: 400)
        .dropDestination(for: String.self) { receivedTitles, location in
            animateDrop(at: location)
            process(titles: receivedTitles)
        } isTargeted: {
            isDropTargeted = $0
        }
}

func process(titles: [String]) { ... }
func animateDrop(at: CGPoint) { ... }
```

## Parameters

- `payloadType`: The expected type of the dropped models.
- `action`: A closure that takes the dropped content and responds   appropriately. The first parameter to   contains the dropped   items. The second   parameter contains the drop location in this view’s coordinate   space. Return   if the drop operation was successful;   otherwise, return  .
- `isTargeted`: A closure that is called when a drag and drop operation   enters or exits the drop target area. The received value is   when   the cursor is inside the area, and   when the cursor is outside.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/siritipview/dropdestination(for:action:istargeted:))*