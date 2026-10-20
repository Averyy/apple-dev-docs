# CNScript.Changes

**Framework**: Cinematic  
**Kind**: struct  
**Role**: Structure

An object that represents a snapshot of the changes made to a movie script, including the added user decisions and detection tracks.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst
- macOS 14.0+
- tvOS 17.0+

## Declaration

```swift
struct Changes
```

#### Overview

Use as a snapshot to quickly revert to previously saved edits.

## Topics

### Initializers
- [init?(dataRepresentation: Data)](./changes/init%28datarepresentation%29.md)
  Creates a previously saved data representation.
### Instance Properties
- [var addedDetectionTracks: [CNDetectionTrack]](./changes/addeddetectiontracks.md)
  All detection tracks added since recording the movie.
- [var dataRepresentation: Data](./changes/datarepresentation.md)
  Persistent data representation of changes for later restoration.
- [var fNumber: Float](./changes/fnumber.md)
  The f/number to apply to the entire movie.
- [var userDecisions: [CNDecision]](./changes/userdecisions.md)
  All active user decisions, including those made at recording time, unless removed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cinematic/cnscript-1ispe/changes)*