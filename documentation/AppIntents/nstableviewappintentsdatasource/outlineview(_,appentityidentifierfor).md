# outlineView(_:appEntityIdentifierFor:)

**Framework**: App Intents  
**Kind**: method  
**Required**: Yes

Asks the data source to return an app entity identifier for a particular item in the outline view.

**Availability**:
- macOS 15.4+

## Declaration

```swift
@MainActor
func outlineView(_ outlineView: NSOutlineView, appEntityIdentifierFor item: Any?) -> EntityIdentifier?
```

#### Return Value

The app entity identifier for the item at the specified location in the outline view.

## Parameters

- `outlineView`: The outline-view object asking for the app entity identifier.
- `item`: The specified item in the outline view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/nstableviewappintentsdatasource/outlineview(_:appentityidentifierfor:))*