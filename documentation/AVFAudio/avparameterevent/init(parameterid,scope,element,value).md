# init(parameterID:scope:element:value:)

**Framework**: AVFAudio  
**Kind**: init  
**Role**: Initializer

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

```objc
- (instancetype) initWithParameterID:(UInt32) parameterID scope:(UInt32) scope element:(UInt32) element value:(float) value;
```

#### Discussion

For more information about the parameters, see [`AudioUnitParameterID`](../../AudioToolbox/audiounitparameterid.md), [`AudioUnitScope`](../../AudioToolbox/audiounitscope.md), and [`AudioUnitElement`](../../AudioToolbox/audiounitelement.md). The valid range of values depend on the parameter you set.

## Parameters

- `parameterID`: The identifier of the parameter.
- `scope`: The audio unit scope for the parameter.
- `element`: The element index in the scope.
- `value`: The value of the parameter to set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avparameterevent/init(parameterid:scope:element:value:))*