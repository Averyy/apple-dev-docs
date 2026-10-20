# parameter(withAddress:)

**Framework**: Audio Toolbox  
**Kind**: method

Searches the tree for a parameter with a specific address.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func parameter(withAddress address: AUParameterAddress) -> AUParameter?
```

#### Return Value

The parameter corresponding to the supplied address, or `nil` if no such parameter exists.

## Parameters

- `address`: The address with which to search the tree.

## See Also

- [func parameter(withID: AudioUnitParameterID, scope: AudioUnitScope, element: AudioUnitElement) -> AUParameter?](auparametertree/parameter(withid:scope:element:).md)
  Searches the tree for a specific version 2 audio unit parameter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/auparametertree/parameter(withaddress:))*