# valuesDidChange

**Framework**: MediaExtension  
**Kind**: property

A notification that indicates a change to the object’s set of available processing parameters.

**Availability**:
- macOS 15.0+

## Declaration

```swift
static let valuesDidChange: NSNotification.Name
```

#### Discussion

This notification is used to notify the client that processor has changed the set of available [`MERAWProcessingParameter`](merawprocessingparameter.md) objects. This includes changing the set of available parameters, changing the enabled state for parameters, or changing default values for parameters. This may occur in response to incoming parameter changes, for example a change in a selected [`MERAWProcessingParameter.ListElement`](merawprocessingparameter/listelement.md), or due to metadata-driven changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaextension/merawprocessornotification/valuesdidchange)*