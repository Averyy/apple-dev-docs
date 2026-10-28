# setEnabled(_:)

**Framework**: Security Interface  
**Kind**: method  
**Role**: Instance Method

Enables or disables the controls in the authorization plug-in’s view.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func setEnabled(_ inEnabled: Bool)
```

```objc
- (void) setEnabled:(BOOL) inEnabled;
```

## Discussion

When the authorization plug-in calls this method, the subclass should call [`setEnabled(_:)`](./setenabled%28_%29.md) on the controls that are in its view.

## Parameters

- `inEnabled`: The state the controls should be in.


---

*[View on Apple Developer](https://developer.apple.com/documentation/securityinterface/sfauthorizationpluginview/setenabled(_:))*