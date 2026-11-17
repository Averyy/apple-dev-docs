# isEnabled

**Framework**: CarPlay  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the item is enabled.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+

## Declaration

```swift
var isEnabled: Bool { get set }
```

```objc
@property (nonatomic, assign, getter=isEnabled) BOOL enabled;
```

## Discussion

When the value of this property is `true`, CarPlay displays the item normally and forwards interactions to the [`handler`](./handler.md) and [`listImageRowHandler`](./listimagerowhandler.md) handlers. When the value of this property is `false`, CarPlay displays the item with a dimmed appearance and doesn’t forward interactions to your handlers. The default value of this property is `true`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cplistimagerowitem/isenabled)*