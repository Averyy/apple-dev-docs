# isEnabled

**Framework**: Safari Services  
**Kind**: property  
**Role**: Instance Property

A flag that indicates whether the universal link is enabled.

**Availability**:
- macOS 10.15+

## Declaration

```swift
var isEnabled: Bool { get set }
```

```objc
@property (getter=isEnabled) BOOL enabled;
```

## Discussion

This Boolean property indicates if the universal link is enabled.

When enabled, this property has two defined behaviors:

1. If an application opens the universal link, the system opens the link in the native application represented by the application URL property instead of the browser.
2. If a browser opens the universal link, it can choose to open the URL using [`open(_:withApplicationAt:configuration:completionHandler:)`](../../AppKit/nsworkspace/open%28_,withapplicationat,configuration,completionhandler%29.md), or can present other information to the user as appropriate.

When this property is disabled, the browser simply opens the URL as it normally would.

## See Also

### Configuring Universal Links
- [var applicationURL: URL](./applicationurl.md)
  The URL to the app that can open this universal link.
- [var webpageURL: URL](./webpageurl.md)
  The URL specified when initializing the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/safariservices/sfuniversallink/isenabled)*