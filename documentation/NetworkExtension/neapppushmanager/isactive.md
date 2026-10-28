# isActive

**Framework**: Network Extension  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether a configuration is in use.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- visionOS 1.0+

## Declaration

```swift
var isActive: Bool { get }
```

```objc
@property (readonly, getter=isActive) BOOL active;
```

## Discussion

Use key-value observing to watch for changes in this property.

## See Also

### Inspecting manager properties
- [var isEnabled: Bool](./isenabled.md)
  A property you use to toggle enabling the configuration.
- [var localizedDescription: String?](./localizeddescription.md)
  A string that contains the localized description of the app push manager.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/neapppushmanager/isactive)*