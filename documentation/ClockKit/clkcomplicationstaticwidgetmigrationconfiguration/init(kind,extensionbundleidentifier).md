# init(kind:extensionBundleIdentifier:)

**Framework**: ClockKit  
**Kind**: init  
**Role**: Initializer

Creates an object that describes a static watchOS complication in your WidgetKit extension.

**Availability**:
- watchOS 9.0+

## Declaration

```swift
init(kind: String, extensionBundleIdentifier: String)
```

```objc
- (instancetype) initWithKind:(NSString *) kind extensionBundleIdentifier:(NSString *) extensionBundleIdentifier;
```

## Parameters

- `kind`: A string that uniquely identifies a widget in your WidgetKit extension.
- `extensionBundleIdentifier`: The bundle identifier for your WidgetKit extension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationstaticwidgetmigrationconfiguration/init(kind:extensionbundleidentifier:))*