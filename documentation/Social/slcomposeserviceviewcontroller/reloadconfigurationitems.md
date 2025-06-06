# reloadConfigurationItems()

**Framework**: Social  
**Kind**: method

Reloads the list of configuration items.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
func reloadConfigurationItems()
```

#### Discussion

In general, a subclass doesn’t need to call this method, unless it determines its configuration items in a deferred way, such as in [`presentationAnimationDidFinish()`](slcomposeserviceviewcontroller/presentationanimationdidfinish().md). In particular, you don’t need to call this method after you change a configuration item property, because the `SLComposeServiceViewController` base class automatically detects and responds to such changes.

## See Also

- [func configurationItems() -> [Any]!](slcomposeserviceviewcontroller/configurationitems.md)
  Returns configuration items to display in the compose view.
- [class SLComposeSheetConfigurationItem](slcomposesheetconfigurationitem.md)
  An object that provides additional configuration details to use when configuring a composition interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/social/slcomposeserviceviewcontroller/reloadconfigurationitems())*