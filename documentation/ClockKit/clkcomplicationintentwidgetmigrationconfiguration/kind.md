# kind

**Framework**: ClockKit  
**Kind**: property  
**Role**: Instance Property

A string that uniquely identifies a widget in your WidgetKit extension.

**Availability**:
- watchOS 9.0+

## Declaration

```swift
var kind: String { get }
```

```objc
@property (nonatomic, copy, readonly) NSString * kind;
```

## See Also

### Accessing configuration properties
- [var extensionBundleIdentifier: String](./extensionbundleidentifier.md)
  The bundle identifier for your WidgetKit extension.
- [var intent: INIntent](./intent.md)
  A SiriKit intent that provides additional configuration information to your WidgetKit complication.
- [var localizedDisplayName: String](./localizeddisplayname.md)
  A localized name for the complication.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationintentwidgetmigrationconfiguration/kind)*