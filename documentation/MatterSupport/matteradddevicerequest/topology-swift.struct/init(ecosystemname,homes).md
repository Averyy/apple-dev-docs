# init(ecosystemName:homes:)

**Framework**: MatterSupport  
**Kind**: init  
**Role**: Initializer

Creates the topology.

**Availability**:
- iOS 16.1+
- iPadOS 16.1+
- Mac Catalyst 16.1+
- macOS 14.0+
- visionOS

## Declaration

```swift
init(ecosystemName: String, homes: [MatterAddDeviceRequest.Home])
```

## Parameters

- `ecosystemName`: The name of your ecosystem. This is a localized string that appears during device setup.
- `homes`: An array of available homes to add the new device into.

## See Also

### Creating the topology
- [init(from: any Decoder) throws](../init%28from%29.md)
  Create the request from a decoder.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mattersupport/matteradddevicerequest/topology-swift.struct/init(ecosystemname:homes:))*