# trackIDs

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The IDs of the tracks in the group.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
var trackIDs: [NSNumber] { get }
```

```objc
@property (nonatomic, readonly) NSArray<NSNumber *> * trackIDs;
```

## Discussion

The value of this property is an array of [`NSNumber`](../../Foundation/nsnumber.md) instances used as [`CMPersistentTrackID`](../../CoreMedia/cmpersistenttrackid.md) values, one for each track in the group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassettrackgroup/trackids)*