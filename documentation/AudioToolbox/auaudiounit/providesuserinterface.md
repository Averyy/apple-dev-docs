# providesUserInterface

**Framework**: Audio Toolbox  
**Kind**: property  
**Role**: Instance Property

A Boolean that indicates whether the audio unit provides a user interface, normally in the form of a view controller.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var providesUserInterface: Bool { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS*

```objc
@property (nonatomic, readonly) BOOL providesUserInterface;
```

*macOS*

```objc
@property (atomic, readonly) BOOL providesUserInterface;
```

## See Also

### Configuring the User Interface
- [func supportedViewConfigurations([AUAudioUnitViewConfiguration]) -> IndexSet](./supportedviewconfigurations%28_%29.md)
- [func select(AUAudioUnitViewConfiguration)](./select%28_%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/providesuserinterface)*