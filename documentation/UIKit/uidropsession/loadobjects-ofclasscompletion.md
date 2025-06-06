# loadObjects(ofClass:completion:)

**Framework**: UIKit  
**Kind**: method  
**Required**: Yes

Creates and loads a new instance of the specified class for each drag item in the session.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func loadObjects(ofClass aClass: any NSItemProviderReading.Type, completion: @escaping ([any NSItemProviderReading]) -> Void) -> Progress
```

## Mentions

- [Making a view into a drop destination](making-a-view-into-a-drop-destination.md)

#### Return Value

An aggregate of the load progress for each object that is loaded.

#### Discussion

You can use this method only in the drop interaction delegate’s implementation of the [`dropInteraction(_:performDrop:)`](uidropinteractiondelegate/dropinteraction(_:performdrop:).md) method. This method is called after the user drops the items into the destination view.

The completion handler is called on the main queue. It provides an array of all objects created, in the same order that the drag items were added to the drag session.

## Parameters

- `aClass`: A class conforming to the   protocol.
- `completion`: The block that is executed after all objects are loaded.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidropsession/loadobjects(ofclass:completion:))*