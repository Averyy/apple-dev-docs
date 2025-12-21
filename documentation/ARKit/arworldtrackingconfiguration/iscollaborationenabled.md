# isCollaborationEnabled

**Framework**: ARKit  
**Kind**: property

A flag that opts you in to a peer-to-peer multiuser AR experience.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+

## Declaration

```swift
var isCollaborationEnabled: Bool { get set }
```

#### Discussion

The default value of this property is [`false`](https://developer.apple.com/documentation/Swift/false). When you enable collaboration, ARKit invokes [`session(_:didOutputCollaborationData:)`](arsessionobserver/session(_:didoutputcollaborationdata:).md) periodically, providing you with collaboration data to share with peers. Collaboration data contains information about the real-world surfaces ARKit detects, your position in relation to them, and any anchors you may have created.

Multiple users sharing collaboration data with each other results in an AR experience in which the users interact by sharing and manipulating anchors. By including information that describes a user’s unique view of the world, collaboration data enhances ARKit’s understanding of the layout of the physical environment much more quickly than is possible with only one user.

For more information, see [`Creating a collaborative session`](creating-a-collaborative-session.md).

> ❗ **Important**:  Collaborative sessions work best with up to four participants.

##### Sharing Collaboration Data Over the Network

You are responsible for sending collaboration data over the network, including choosing the network framework and implementing the code. See [`Creating a multiuser AR experience`](creating-a-multiuser-ar-experience.md) for an example app that shares a world map among users via [`Multipeer Connectivity`](https://developer.apple.com/documentation/MultipeerConnectivity). Although [`Creating a multiuser AR experience`](creating-a-multiuser-ar-experience.md) demonstrates sharing world data among peer users, it does so using a host-guest model. The primary advantage of collaboration data is that it enables you to share world data peer-to-peer.

The data you send is a serialized version of the [`ARSession.CollaborationData`](arsession/collaborationdata.md) object provided by your session. You serialize it using [`NSKeyedArchiver`](https://developer.apple.com/documentation/Foundation/NSKeyedArchiver).

```swift
func session(_ session: ARSession, didOutputCollaborationData data: ARSession.CollaborationData) {    
    if let collaborationDataEncoded = try? NSKeyedArchiver.archivedData(withRootObject: data, requiringSecureCoding: true) {
        multipeerSession.sendToAllPeers(collaborationDataEncoded)
    } else {
        fatalError("An error occurred while encoding collaboration data.")
    }
}
```

##### Updating Your Session with Collaboration Data

When you receive collaboration data from other people, you instantiate an [`ARSession.CollaborationData`](arsession/collaborationdata.md) object with it and pass the object to your session with [`update(with:)`](arsession/update(with:).md). For optimum performance, it’s helpful if the participants in a collaborative session are on the same OS version. Unarchiving `ARSession.CollaborationData` received from a device running a different OS version may fail.

```swift
func receivedData(_ data: Data) {        
    if let collaborationData = try? NSKeyedUnarchiver.unarchivedObject(ofClass: ARSession.CollaborationData.self, from: data) {
        session.update(with: collaborationData)
    } else {
        print("A device running an incompatible OS version is in the collaborative session.")
    }
}

```


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arworldtrackingconfiguration/iscollaborationenabled)*