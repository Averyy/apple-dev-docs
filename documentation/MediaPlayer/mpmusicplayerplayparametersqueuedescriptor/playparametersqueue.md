# playParametersQueue

**Framework**: Media Player  
**Kind**: property  
**Role**: Instance Property

An array containing the play parameters returned from querying MusicKit.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
var playParametersQueue: [MPMusicPlayerPlayParameters] { get set }
```

```objc
@property (nonatomic, copy) NSArray<MPMusicPlayerPlayParameters *> * playParametersQueue;
```

## See Also

### Accessing the play parameters
- [var startItemPlayParameters: MPMusicPlayerPlayParameters?](./startitemplayparameters.md)
  The item identified by the play parameters to play first.
- [class MPMusicPlayerPlayParameters](../mpmusicplayerplayparameters.md)
  The MusicKit parameters that describe items to play.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpmusicplayerplayparametersqueuedescriptor/playparametersqueue)*