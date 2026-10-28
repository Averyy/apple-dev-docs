# CNScriptChanges

**Framework**: Cinematic  
**Kind**: class  
**Role**: Class

An object that represents a snapshot of the changes made to a movie script, including the added user decisions and detection tracks.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+

## Declaration

```objc
@interface CNScriptChanges : NSObject
```

## Overview

Use as a snapshot to quickly revert to previously saved edits.

## Topics

### Instance Properties
- [addedDetectionTracks](./cnscriptchanges/addeddetectiontracks.md)
  All detection tracks added since recording the movie.
- [dataRepresentation](./cnscriptchanges/datarepresentation.md)
  Persistent data representation of changes for later restoration.
- [fNumber](./cnscriptchanges/fnumber.md)
  The f-stop number to apply to the entire movie.
- [userDecisions](./cnscriptchanges/userdecisions.md)
  All active user decisions, including those made at recording time, unless removed.
### Instance Methods
- [- initWithDataRepresentation:](./cnscriptchanges/initwithdatarepresentation_.md)
  Creates a previously saved data representation.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)

## See Also

### Essentials
- [Playing and editing Cinematic mode video](./playing-and-editing-cinematic-mode-video.md)
  Play and edit Cinematic mode video with an adjustable depth of field and focus points.
- [CNScript](./cnscript-9e1zn.md)
  A collection of focus decisions, focus transitions, detections, and detection tracks associated with a movie captured in Cinematic mode and methods to change them.
- [CNScriptFrame](./cnscriptframe.md)
  An object that represents what to focus on, and where to focus, in a given movie frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cinematic/cnscriptchanges)*