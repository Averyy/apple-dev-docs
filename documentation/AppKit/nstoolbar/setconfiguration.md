# setConfiguration(_:)

**Framework**: AppKit  
**Kind**: method

Specifies the new configuration details for the toolbar.

**Availability**:
- macOS 10.0+

## Declaration

```swift
@MainActor
func setConfiguration(_ configDict: [String : Any])
```

#### Discussion

If you implement your own autosave mechanism, call this method to restore the configuration of your toolbar to a previously saved state. The dictionary you read from disk must match the format of the dictionary in the [`configuration`](nstoolbar/configuration.md) property.

## Parameters

- `configDict`: A dictionary with the toolbar configuration details. The toolbar ignores any keys it doesn’t recognize. Typically, you save the original configuration dictionary from the   property to disk and recreate it before passing it in this parameter.

## See Also

- [var autosavesConfiguration: Bool](nstoolbar/autosavesconfiguration.md)
  A Boolean value that indicates whether the toolbar autosaves its configuration.
- [var configuration: [String : Any]](nstoolbar/configuration.md)
  A dictionary containing the current configuration details for the toolbar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstoolbar/setconfiguration(_:))*