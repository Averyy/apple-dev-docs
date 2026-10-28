# widgetKind

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

An identifier that associates the shortcut with the widget it influences.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
var widgetKind: String? { get set }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, nullable) NSString * widgetKind;
```

*macOS*

```objc
@property (atomic, copy, nullable) NSString * widgetKind;
```

## Discussion

To provide relevance information for a widget, use the same value for this property as for the [`kind`](../../WidgetKit/widgetinfo/kind.md) property of the widget’s configuration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inrelevantshortcut/widgetkind)*