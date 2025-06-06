# setFontPanelFactory(_:)

**Framework**: AppKit  
**Kind**: method

Sets the class that creates the shared Font panel object.

**Availability**:
- macOS ?+

## Declaration

```swift
class func setFontPanelFactory(_ factoryId: AnyClass?)
```

#### Discussion

Call this method before accessing the Font panel in any way, such as in your app delegate’s [`applicationWillFinishLaunching(_:)`](nsapplicationdelegate/applicationwillfinishlaunching(_:).md) method.

## Parameters

- `factoryId`: The new font panel factory class, which should be a subclass of  .

## See Also

- [class func setFontManagerFactory(AnyClass?)](nsfontmanager/setfontmanagerfactory(_:).md)
  Sets the class that creates the shared font manager object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsfontmanager/setfontpanelfactory(_:))*