# isEnabled

**Framework**: Authentication Services  
**Kind**: property  
**Role**: Instance Property

A Boolean value indicating whether the credential identity store is enabled.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var isEnabled: Bool { get }
```

```objc
@property (nonatomic, readonly, getter=isEnabled) BOOL enabled;
```

## Discussion

You can only modify a credential identity store that’s enabled.

## See Also

### Checking the state
- [var supportsIncrementalUpdates: Bool](./supportsincrementalupdates.md)
  A Boolean value indicating whether the credential identity store supports incremental updates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/ascredentialidentitystorestate/isenabled)*