# localizedDisplayName

**Framework**: Network Extension  
**Kind**: property  
**Required**: Yes

A localized string that the system UI uses for annotation of the Wi-Fi network.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- visionOS 26.0+

## Declaration

```swift
var localizedDisplayName: String { get }
```

#### Discussion

The framework uses this property only if the evaluation provider responds to the [`NEHotspotHelperCommandType.filterScanList`](nehotspothelpercommandtype/filterscanlist.md) command with a [`NEHotspotHelperResult.success`](nehotspothelperresult/success.md) result, and the network list contains the Wi-Fi network.

If the framework doesn’t use your provider for hotspot evaluation and the hotspot manager’s [`evaluatedSSIDs`](nehotspotmanager/evaluatedssids.md) property contains valid SSIDs, it uses a system-defined localized string instead of this property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nehotspotevaluationprovider/localizeddisplayname)*