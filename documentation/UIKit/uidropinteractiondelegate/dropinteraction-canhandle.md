# dropInteraction(_:canHandle:)

**Framework**: Uikit  
**Kind**: method

Asks the delegate whether it can handle the session’s drag items.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func dropInteraction(_ interaction: UIDropInteraction, canHandle session: any UIDropSession) -> Bool
```

## Mentions

- [Making a view into a drop destination](making-a-view-into-a-drop-destination.md)

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the interaction supports the drag items in the sessions; otherwise, [`false`](https://developer.apple.com/documentation/swift/false).

#### Discussion

Returning [`true`](https://developer.apple.com/documentation/swift/true) doesn’t mean the interaction will accept the drop. Instead, it tells the system that the interaction has interest in, and can handle, the drop session.

To determine if the interaction can handle the session, check the data type of session’s drag items. For instance, if you’re interested in drop activities that contain images, you can do the following:

```swift
func dropInteraction(_ interaction: UIDropInteraction, canHandle session: UIDropSession) -> Bool {
    // Ensure the drop session has an object of the appropriate type
    return session.canLoadObjects(ofClass: UIImage.self)
}
```

You can also be more specific by using a uniform type identifier (UTI) for the data type. For instance, if you’re interested in only PNG images, use the UTI for PNG files:

```swift
import MobileCoreServices // for kUTTypePNG

func dropInteraction(_ interaction: UIDropInteraction, canHandle session: UIDropSession) -> Bool {
    return session.hasItemsConforming(toTypeIdentifiers: [kUTTypePNG as String])
}
```

> **Note**:  You can’t check the actual data the user is dragging because it isn’t available when the interaction calls this method. Only the data type is available inside this method.

## Parameters

- `interaction`: The interaction that called this method.
- `session`: The current drop session.

## See Also

- [func dropInteraction(UIDropInteraction, performDrop: any UIDropSession)](uidropinteractiondelegate/dropinteraction(_:performdrop:).md)
  Tells the delegate it can request the item provider data from the session’s drag items.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidropinteractiondelegate/dropinteraction(_:canhandle:))*