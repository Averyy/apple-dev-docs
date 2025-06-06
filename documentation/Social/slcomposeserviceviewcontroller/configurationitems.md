# configurationItems()

**Framework**: Social  
**Kind**: method

Returns configuration items to display in the compose view.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
func configurationItems() -> [Any]!
```

#### Return Value

An array of [`SLComposeSheetConfigurationItem`](slcomposesheetconfigurationitem.md) objects, or `nil` if no configuration items need to be displayed.

#### Discussion

Implement this method if you need to display configuration items, such as an account picker or privacy indicator, in your compose view.

## See Also

- [class SLComposeSheetConfigurationItem](slcomposesheetconfigurationitem.md)
  An object that provides additional configuration details to use when configuring a composition interface.
- [func reloadConfigurationItems()](slcomposeserviceviewcontroller/reloadconfigurationitems.md)
  Reloads the list of configuration items.


---

*[View on Apple Developer](https://developer.apple.com/documentation/social/slcomposeserviceviewcontroller/configurationitems())*