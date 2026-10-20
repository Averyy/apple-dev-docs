# setConfiguration(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Specifies the new configuration details for the toolbar.

**Availability**:
- macOS 10.0+ - Deprecated in 15.0

> **Deprecated**: Use -setItemIdentifiers: and -setDisplayMode: instead.

## Declaration

```swift
func setConfiguration(_ configDict: [String : Any])
```

```objc
- (void) setConfigurationFromDictionary:(NSDictionary<NSString *,id> *) configDict;
```

#### Discussion

If you implement your own autosave mechanism, call this method to restore the configuration of your toolbar to a previously saved state. The dictionary you read from disk must match the format of the dictionary in the [`configuration`](./configuration.md) property.

## Parameters

- `configDict`: A dictionary with the toolbar configuration details. The toolbar ignores any keys it doesn’t recognize. Typically, you save the original configuration dictionary from the [`configuration`](./configuration.md) property to disk and recreate it before passing it in this parameter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstoolbar/setconfiguration(_:))*