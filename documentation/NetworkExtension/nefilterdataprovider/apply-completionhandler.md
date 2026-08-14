# apply(_:completionHandler:)

**Framework**: Network Extension  
**Kind**: method

Applies a set of filtering rules associated with the provider and changes the default filtering action.

**Availability**:
- macOS 10.15+

## Declaration

```swift
func apply(_ settings: NEFilterSettings?) async throws
```

## Parameters

- `settings`: A [`NEFilterSettings`](nefiltersettings.md) object containing the filter settings to apply to the system. Pass `nil` to revert to the default settings, which are an empty list of rules and a default action of [`NEFilterAction.filterData`](nefilteraction/filterdata.md).
- `completionHandler`: A Swift closure or ObjectiveC block that executes when the system finishes applying the settings. It receives an [`NSError`](https://developer.apple.com/documentation/foundation/nserror) parameter; a non-`nil` value that indicates there’s an error contidition.

## See Also

- [class NEFilterSettings](nefiltersettings.md)
  The rules and other settings that define the operation of a filter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nefilterdataprovider/apply(_:completionhandler:))*