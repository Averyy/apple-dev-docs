# setFontPanelFactory(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Type Method

Sets the class that creates the shared Font panel object.

**Availability**:
- macOS

## Declaration

```swift
class func setFontPanelFactory(_ factoryId: AnyClass?)
```

```objc
+ (void) setFontPanelFactory:(Class) factoryId;
```

#### Discussion

Call this method before accessing the Font panel in any way, such as in your app delegate’s [`applicationWillFinishLaunching(_:)`](../nsapplicationdelegate/applicationwillfinishlaunching%28_%29.md) method.

## Parameters

- `factoryId`: The new font panel factory class, which should be a subclass of `NSFontPanel`.

## See Also

### Changing the Default Font Conversion Classes
- [class func setFontManagerFactory(AnyClass?)](./setfontmanagerfactory%28_%29.md)
  Sets the class that creates the shared font manager object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsfontmanager/setfontpanelfactory(_:))*