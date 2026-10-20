# supportedViewConfigurations(_:)

**Framework**: Audio Toolbox  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- visionOS 1.0+

## Declaration

```swift
func supportedViewConfigurations(_ availableViewConfigurations: [AUAudioUnitViewConfiguration]) -> IndexSet
```

```objc
- (NSIndexSet *) supportedViewConfigurations:(NSArray<AUAudioUnitViewConfiguration *> *) availableViewConfigurations;
```

## See Also

### Configuring the User Interface
- [var providesUserInterface: Bool](./providesuserinterface.md)
  A Boolean that indicates whether the audio unit provides a user interface, normally in the form of a view controller.
- [func select(AUAudioUnitViewConfiguration)](./select%28_%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/supportedviewconfigurations(_:))*