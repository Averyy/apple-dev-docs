# init(for:)

**Framework**: AudioAccessoryKit  
**Kind**: init

Creates a sensor update sequence for the specified accessory.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)

## Declaration

```swift
init(for accessoryIdentifier: String)
```

#### Discussion

Multiple iterators created from the same value — or from copies of it — all receive every packet over a single shared XPC connection. No XPC resources are acquired until the first iteration begins.

## Parameters

- `accessoryIdentifier`: The UID identifying the accessory, obtained from the `AudioUnit` initialization parameters passed to the Audio Rendering Extension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audioaccessorykit/accessorysensorupdates/init(for:))*