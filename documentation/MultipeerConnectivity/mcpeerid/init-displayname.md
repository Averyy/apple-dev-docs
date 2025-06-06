# init(displayName:)

**Framework**: Multipeer Connectivity  
**Kind**: init

Initializes a peer.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
init(displayName myDisplayName: String)
```

#### Return Value

An initialized peer ID object.

#### Discussion

Call this method  when creating the local peer, not when you create objects that represent other devices.

This method throws an exception if the `displayName` value is too long, empty, or `nil`.

Each call to this method produces a unique peer ID, even for the same display name. If you need a device to maintain a consistent peer ID over time, you may want to archive and reuse it later instead of creating a new one every time your app starts advertising or browsing.

## Parameters

- `myDisplayName`: The display name is intended for use in UI elements, and should be short and descriptive of the local peer. The maximum allowable length is 63 bytes in UTF-8 encoding. The   parameter may not be   or an empty string.

## See Also

- [var displayName: String](mcpeerid/displayname.md)
  The display name for this peer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/multipeerconnectivity/mcpeerid/init(displayname:))*