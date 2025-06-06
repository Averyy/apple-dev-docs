# originator

**Framework**: Avfoundation  
**Kind**: property

The participant that causes the coordinator to issue the command.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
var originator: AVCoordinatedPlaybackParticipant? { get }
```

#### Discussion

Only commands that the system issues on behalf of another participant contain an originator. Local commands to coordinate rate change, or those that originate from a call to [`reapplyCurrentItemStateToPlaybackControlDelegate()`](avdelegatingplaybackcoordinator/reapplycurrentitemstatetoplaybackcontroldelegate().md), don’t.

> **Note**:  You can use the existance of an originator value to show a user interface that indicates another partipant’s action.

## See Also

- [var expectedCurrentItemIdentifier: String](avdelegatingplaybackcoordinatorplaybackcontrolcommand/expectedcurrentitemidentifier.md)
  An item identifier the coordinator issues the command for.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avdelegatingplaybackcoordinatorplaybackcontrolcommand/originator)*