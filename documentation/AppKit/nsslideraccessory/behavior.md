# behavior

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The effect on interaction with the accessory.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.12+

## Declaration

```swift
@NSCopying
var behavior: NSSliderAccessoryBehavior { get set }
```

```objc
@property (copy) NSSliderAccessoryBehavior * behavior;
```

#### Discussion

The default value is `automaticBehavior`.

## See Also

### Instance Properties
- [var isEnabled: Bool](./isenabled.md)
  Determines whether or not the accessory is interactive and draws with an enabled appearance. Defaults to `true`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsslideraccessory/behavior)*