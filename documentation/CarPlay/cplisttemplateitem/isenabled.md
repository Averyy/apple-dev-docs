# isEnabled

**Framework**: CarPlay  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

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

When the value of this property is `true`, CarPlay displays the item normally and allows interactions to occur. When the value of this property is `false`, CarPlay displays the item with a dimmed appearance and doesn’t allow interactions. The default value of this property is `true`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cplisttemplateitem/isenabled)*