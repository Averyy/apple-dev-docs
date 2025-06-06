# displayName

**Framework**: Multipeer Connectivity  
**Kind**: property

The display name for this peer.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
var displayName: String { get }
```

#### Discussion

For the local peer, you set this property when the object is initialized. It cannot be changed.

For other peer objects provided to you by the framework, this property is provided by the peer and cannot be changed.

## See Also

- [init(displayName: String)](mcpeerid/init(displayname:).md)
  Initializes a peer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/multipeerconnectivity/mcpeerid/displayname)*