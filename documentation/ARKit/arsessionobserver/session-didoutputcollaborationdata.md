# session(_:didOutputCollaborationData:)

**Framework**: ARKit  
**Kind**: method

Provides information for nearby users about your perspective in the environment.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+

## Declaration

```swift
optional func session(_ session: ARSession, didOutputCollaborationData data: ARSession.CollaborationData)
```

#### Discussion

The data parameter contains information about your perspective in the physical environment. When ARKit invokes this function, send the `data` object to nearby users. The users update their session with your data to gain your app’s model of the physical environment in addition to their own. For more information, see [`isCollaborationEnabled`](arworldtrackingconfiguration/iscollaborationenabled.md).

For an example app that implements this callback, see [`Creating a collaborative session`](creating-a-collaborative-session.md).

## Parameters

- `session`: The app’s collaborative session.
- `data`: The information to share with participants.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arsessionobserver/session(_:didoutputcollaborationdata:))*