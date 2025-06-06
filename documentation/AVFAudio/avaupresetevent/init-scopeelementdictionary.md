# init(scope:element:dictionary:)

**Framework**: AVFAudio  
**Kind**: init

Creates an event with the scope, element, and dictionary for the preset.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
init(scope: UInt32, element: UInt32, dictionary presetDictionary: [AnyHashable : Any])
```

#### Discussion

The system copies the dictionary you specify and isn’t editable once it creates the event. The `scope` parameter must be [`kAudioUnitScope_Global`](https://developer.apple.com/documentation/AudioToolbox/kAudioUnitScope_Global), and the element index should be `0`.

## Parameters

- `scope`: The audio unit scope.
- `element`: The element index in the scope.
- `presetDictionary`: The dictionary that contains the preset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaupresetevent/init(scope:element:dictionary:))*