# applying(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Creates a configuration object by applying the values from the configuration you specify.

**Availability**:
- macOS 12.0+

## Declaration

```swift
func applying(_ configuration: NSImage.SymbolConfiguration) -> Self
```

```objc
- (instancetype) configurationByApplyingConfiguration:(NSImageSymbolConfiguration *) configuration;
```

## Return Value

A new configuration object that prioritizes the values from the configuration you specify.

## Parameters

- `configuration`: The configuration details to apply.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsimage/symbolconfiguration-swift.class/applying(_:))*