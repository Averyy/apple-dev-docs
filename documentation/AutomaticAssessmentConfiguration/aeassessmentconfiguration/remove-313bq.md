# remove(_:)

**Framework**: Automatic Assessment Configuration  
**Kind**: method

Removes the availability of a previously allowed app.

**Availability**:
- iOS 17.5+
- iPadOS 17.5+
- Mac Catalyst 15.0+
- macOS 12.0+

## Declaration

```swift
func remove(_ application: AEAssessmentApplication)
```

#### Discussion

Use this method to remove apps that you previously added to the list of apps that are available during an assessment with the `AEAssessmentConfiguration/setConfiguration(_:for:)` method. You can get the list of currently allowed apps by accessing the configuration’s [`configurationsByApplication`](aeassessmentconfiguration/configurationsbyapplication.md) property.

## Parameters

- `application`: The app that you want to remove from the list of allowed secondary apps.


---

*[View on Apple Developer](https://developer.apple.com/documentation/automaticassessmentconfiguration/aeassessmentconfiguration/remove(_:)-313bq)*