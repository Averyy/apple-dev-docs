# burstSelectionTypes

**Framework**: Photos  
**Kind**: property  
**Role**: Instance Property

The selection type of the asset in a burst photo sequence.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
var burstSelectionTypes: PHAssetBurstSelectionType { get }
```

```objc
@property (nonatomic, assign, readonly) PHAssetBurstSelectionType burstSelectionTypes;
```

#### Discussion

When the user takes a sequence of photos in burst mode with the Camera app (on supported devices), the Photos app user interface groups the resulting assets together and allows the user to select favorite members of the sequence. Photos also automatically marks members of the sequence as potential user favorites. See [`PHAssetBurstSelectionType`](../phassetburstselectiontype.md) for possible values.

Because an asset may have more than one selection type, you use bit masks to identify an asset. For example, the code below tests an asset’s selection type.

**Swift**:

```swift
if (burstSelectionTypes.rawValue == (PHAssetBurstSelectionType.autoPick.rawValue |  PHAssetBurstSelectionType.userPick.rawValue)) {
    print("Display two badges in the user interface.")
} else if (burstSelectionTypes == .autoPick) {
    print("Display an auto-selected badge in the user interface.")
} else if (burstSelectionTypes == .userPick) {
    print("Display a user-selected badge in the user interface.")
}
```

**Objective-C**:

```objc
if (asset.burstSelectionTypes & (PHAssetBurstSelectionTypeAutoPick | PHAssetBurstSelectionTypeUserPick)) {
    // Display two badges in the user interface.
} else if (asset.burstSelectionTypes & PHAssetBurstSelectionTypeAutoPick)) {
    // Display an auto-selected badge in the user interface.
} else if (asset.burstSelectionTypes & PHAssetBurstSelectionTypeUserPick)) {
    // Display a user-selected badge in the user interface.
}
```

## See Also

### Working with Burst Photo Assets
- [var burstIdentifier: String?](./burstidentifier.md)
  The unique identifier shared by photo assets from the same burst sequence.
- [struct PHAssetBurstSelectionType](../phassetburstselectiontype.md)
  Bit mask values indicating whether and how an asset is marked as a favorite member of a burst photo sequence. Used by the [`burstSelectionTypes`](./burstselectiontypes.md) property.
- [var representsBurst: Bool](./representsburst.md)
  A Boolean value that indicates whether the asset is the representative photo from a burst photo sequence.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phasset/burstselectiontypes)*