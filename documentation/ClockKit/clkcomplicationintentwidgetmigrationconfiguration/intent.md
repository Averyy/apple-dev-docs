# intent

**Framework**: ClockKit  
**Kind**: property  
**Role**: Instance Property

A SiriKit intent that provides additional configuration information to your WidgetKit complication.

**Availability**:
- watchOS 9.0+

## Declaration

```swift
@NSCopying
var intent: INIntent { get }
```

```objc
@property (nonatomic, copy, readonly) INIntent * intent;
```

## See Also

### Accessing configuration properties
- [var kind: String](./kind.md)
  A string that uniquely identifies a widget in your WidgetKit extension.
- [var extensionBundleIdentifier: String](./extensionbundleidentifier.md)
  The bundle identifier for your WidgetKit extension.
- [var localizedDisplayName: String](./localizeddisplayname.md)
  A localized name for the complication.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationintentwidgetmigrationconfiguration/intent)*