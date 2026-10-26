# representsBurst

**Framework**: Photos  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the asset is the representative photo from a burst photo sequence.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
var representsBurst: Bool { get }
```

```objc
@property (nonatomic, assign, readonly) BOOL representsBurst;
```

#### Discussion

When the user takes a sequence of photos in burst mode with the Camera app (on supported devices), the Photos app user interface groups the resulting assets together. One asset represents the entire sequence in displayed collections.

## See Also

### Working with Burst Photo Assets
- [var burstIdentifier: String?](./burstidentifier.md)
  The unique identifier shared by photo assets from the same burst sequence.
- [var burstSelectionTypes: PHAssetBurstSelectionType](./burstselectiontypes.md)
  The selection type of the asset in a burst photo sequence.
- [struct PHAssetBurstSelectionType](../phassetburstselectiontype.md)
  Bit mask values indicating whether and how an asset is marked as a favorite member of a burst photo sequence. Used by the [`burstSelectionTypes`](./burstselectiontypes.md) property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phasset/representsburst)*