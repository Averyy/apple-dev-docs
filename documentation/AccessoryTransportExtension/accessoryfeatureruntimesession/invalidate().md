# invalidate()

**Framework**: Accessory Transport Extension  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Unregisters the session.

**Availability**:
- iOS 27.3+ (Beta)

## Declaration

```swift
func invalidate()
```

## Discussion

Call this method when your app’s exchange with the data provider extension is complete but before releasing an active session. The system throws an error if your app releases an active session without invalidating it.

## Default Implementations

### AccessoryFeatureRuntimeSession Implementations
- [func invalidate()](./invalidate%28%29-6sewy.md)

## See Also

### Managing the session life cycle
- [func activate() async throws](./activate%28%29.md)
  Registers the session and requests that the system start it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorytransportextension/accessoryfeatureruntimesession/invalidate())*