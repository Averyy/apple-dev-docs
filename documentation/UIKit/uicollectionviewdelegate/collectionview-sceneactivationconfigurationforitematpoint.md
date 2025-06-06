# collectionView(_:sceneActivationConfigurationForItemAt:point:)

**Framework**: UIKit  
**Kind**: method

Returns a scene activation configuration that allows the cell to expand into a new scene.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func collectionView(_ collectionView: UICollectionView, sceneActivationConfigurationForItemAt indexPath: IndexPath, point: CGPoint) -> UIWindowScene.ActivationConfiguration?
```

#### Return Value

A [`UIWindowScene.ActivationConfiguration`](uiwindowscene/activationconfiguration.md) object that facilitates expanding the cell into a new scene. Return `nil` to prevent the interaction from starting.

## Parameters

- `collectionView`: The collection view.
- `indexPath`: The index path of the cell with which the user is interacting.
- `point`: The location of the interaction in the collection view’s coordinate space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewdelegate/collectionview(_:sceneactivationconfigurationforitemat:point:))*