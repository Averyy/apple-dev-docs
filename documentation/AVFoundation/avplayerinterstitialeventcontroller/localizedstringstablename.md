# localizedStringsTableName

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The name of the table in the bundle that contains the localized strings to be used by the AVPlayerInterstitialEventController.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
var localizedStringsTableName: String? { get set }
```

```objc
@property (copy, nullable) NSString * localizedStringsTableName;
```

## Discussion

If the value of the property is nil, it will default to “Localizable”

## See Also

### Accessing strings
- [var localizedStringsBundle: Bundle?](./localizedstringsbundle.md)
  The bundle that contains the localized strings to be used by the AVPlayerInterstitialEventController.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayerinterstitialeventcontroller/localizedstringstablename)*