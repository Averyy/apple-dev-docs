# onLongPressGesture(minimumDuration:maximumDistance:pressing:perform:)

**Framework**: FamilyControls  
**Kind**: method

Adds an action to perform when this view recognizes a long press gesture.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- visionOS ?+
- watchOS 6.0+

## Declaration

```swift
nonisolated
func onLongPressGesture(minimumDuration: Double = 0.5, maximumDistance: CGFloat = 10, pressing: ((Bool) -> Void)? = nil, perform action: @escaping () -> Void) -> some View
```

## See Also

- [func onLongPressGesture(minimumDuration: Double, pressing: ((Bool) -> Void)?, perform: () -> Void) -> some View](familyactivitypicker/onlongpressgesture(minimumduration:pressing:perform:).md)
  Adds an action to perform when this view recognizes a long press gesture.
- [func onDrop(of: [String], delegate: any DropDelegate) -> some View](familyactivitypicker/ondrop(of:delegate:)-3cx1m.md)
  Defines the destination for a drag and drop operation with the same size and position as this view, with behavior controlled by the given delegate.
- [func onDrop(of: [String], isTargeted: Binding<Bool>?, perform: ([NSItemProvider], CGPoint) -> Bool) -> some View](familyactivitypicker/ondrop(of:istargeted:perform:)-647xj.md)
  Defines the destination for a drag and drop operation with the same size and position as this view, handling dropped content and the drop location with the given closure.
- [func onDrop(of: [String], isTargeted: Binding<Bool>?, perform: ([NSItemProvider]) -> Bool) -> some View](familyactivitypicker/ondrop(of:istargeted:perform:)-6kw8i.md)
  Defines the destination for a drag and drop operation, using the same size and position as this view, handling dropped content with the given closure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/familycontrols/familyactivitypicker/onlongpressgesture(minimumduration:maximumdistance:pressing:perform:))*