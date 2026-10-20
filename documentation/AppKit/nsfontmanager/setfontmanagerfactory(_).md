# setFontManagerFactory(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Type Method

Sets the class that creates the shared font manager object.

**Availability**:
- macOS

## Declaration

```swift
class func setFontManagerFactory(_ factoryId: AnyClass?)
```

```objc
+ (void) setFontManagerFactory:(Class) factoryId;
```

#### Discussion

When you call the [`shared`](./shared.md) method of [`NSFontManager`](../nsfontmanager.md), it creates an instance of `aClass`, if no instance already exists. The class in `aClass` must implement `init` as its designated initializer. The default font manager factory is `NSFontManager`.

Call this method before AppKit loads your application’s main nib file, such as in your app’s `main` function before calling `NSApplicationMain`, or in the `init` method of your [`NSApplication`](../nsapplication.md) subclass. Call this method early, since AppKit calls your app delegate’s [`applicationWillFinishLaunching(_:)`](../nsapplicationdelegate/applicationwillfinishlaunching%28_%29.md) method after it has loaded the main nib file.

## Parameters

- `factoryId`: The new font manager factory class, which must be a subclass of [`NSFontManager`](../nsfontmanager.md).

## See Also

### Changing the Default Font Conversion Classes
- [class func setFontPanelFactory(AnyClass?)](./setfontpanelfactory%28_%29.md)
  Sets the class that creates the shared Font panel object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsfontmanager/setfontmanagerfactory(_:))*