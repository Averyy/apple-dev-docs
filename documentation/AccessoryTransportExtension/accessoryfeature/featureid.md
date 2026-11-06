# featureID

**Framework**: Accessory Transport Extension  
**Kind**: property  
**Role**: Type Property  
**Required**: Yes

A string for the feature type.

**Availability**:
- iOS 26.5+

## Declaration

```swift
static var featureID: String { get }
```

## Discussion

List this value under the `EXCapabilities` key in your data provider extension’s target properties. Use the same value for every app that declares the feature.

> ❗ **Important**: The value of this property isn’t always equal to the transport message’s [`sessionID`](../transportmessage/sessionid.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorytransportextension/accessoryfeature/featureid)*