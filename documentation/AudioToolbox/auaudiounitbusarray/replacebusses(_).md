# replaceBusses(_:)

**Framework**: Audio Toolbox  
**Kind**: method  
**Role**: Instance Method

Replaces the current bus array with a copy of the supplied bus array.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```swift
func replaceBusses(_ busArray: [AUAudioUnitBus])
```

```objc
- (void) replaceBusses:(NSArray<AUAudioUnitBus *> *) busArray;
```

## Discussion

The base class issues KVO notifications.

## Parameters

- `busArray`: The new bus array.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/auaudiounitbusarray/replacebusses(_:))*