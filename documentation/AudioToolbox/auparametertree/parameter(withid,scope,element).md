# parameter(withID:scope:element:)

**Framework**: Audio Toolbox  
**Kind**: method  
**Role**: Instance Method

Searches the tree for a specific version 2 audio unit parameter.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func parameter(withID paramID: AudioUnitParameterID, scope: AudioUnitScope, element: AudioUnitElement) -> AUParameter?
```

```objc
- (AUParameter *) parameterWithID:(AudioUnitParameterID) paramID scope:(AudioUnitScope) scope element:(AudioUnitElement) element;
```

#### Return Value

The parameter corresponding to the supplied ID, scope, and element. Returns `nil` if the parameter is nonexistent or if it is not associated with a version 2 audio unit.

#### Discussion

Version 2 audio units publish parameters identified by a parameter ID, scope, and element. A host that knows that it is dealing with a version 2 audio unit can locate parameters using this method—for example, for the Apple-supplied system audio units.

## Parameters

- `paramID`: The parameter ID with which to search the tree.
- `scope`: The scope with which to search the tree.
- `element`: The element with which to search the tree.

## See Also

### Obtaining Tree Parameters
- [func parameter(withAddress: AUParameterAddress) -> AUParameter?](./parameter%28withaddress%29.md)
  Searches the tree for a parameter with a specific address.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/auparametertree/parameter(withid:scope:element:))*