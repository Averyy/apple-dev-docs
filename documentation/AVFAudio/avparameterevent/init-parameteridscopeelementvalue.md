# init(parameterID:scope:element:value:)

**Framework**: AVFAudio  
**Kind**: init

Creates an event with a parameter identifier, scope, element, and value for the parameter to set.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
init(parameterID: UInt32, scope: UInt32, element: UInt32, value: Float)
```

#### Discussion

For more information about the parameters, see [`AudioUnitParameterID`](https://developer.apple.com/documentation/AudioToolbox/AudioUnitParameterID), [`AudioUnitScope`](https://developer.apple.com/documentation/AudioToolbox/AudioUnitScope), and [`AudioUnitElement`](https://developer.apple.com/documentation/AudioToolbox/AudioUnitElement). The valid range of values depend on the parameter you set.

## Parameters

- `parameterID`: The identifier of the parameter.
- `scope`: The audio unit scope for the parameter.
- `element`: The element index in the scope.
- `value`: The value of the parameter to set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avparameterevent/init(parameterid:scope:element:value:))*