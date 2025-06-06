# setInterstitialMediaSelectionCriteria(_:forMediaCharacteristic:)

**Framework**: AVFoundation  
**Kind**: method

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- tvOS 18.4+
- visionOS 2.4+
- watchOS 11.4+

## Declaration

```swift
func setInterstitialMediaSelectionCriteria(_ criteria: [AVPlayerMediaSelectionCriteria], forMediaCharacteristic mediaCharacteristic: AVMediaCharacteristic)
```

#### Discussion

```None
			This method allows the user to specify AVMediaSelectionCriteria for all interstitials that are discovered.
			Each AVPlayerMediaSelectionCriteria in the array of criteria specfies a set of criteria for a variant to download.
```

## Parameters

- `criteria`: The array of selection criteria to set
- `mediaCharacteristic`: The AVMediaCharacteristic to which the criteria will be applied


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetdownloadconfiguration/setinterstitialmediaselectioncriteria(_:formediacharacteristic:))*