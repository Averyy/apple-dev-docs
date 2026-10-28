# actions

**Framework**: CarPlay  
**Kind**: property  
**Role**: Instance Property

The array of actions available on the alert.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
var actions: [CPAlertAction] { get }
```

```objc
@property (nonatomic, strong, readonly) NSArray<CPAlertAction *> * actions;
```

## Discussion

The array must include at least one action.

## See Also

### Getting the Alert Information
- [var titleVariants: [String]](./titlevariants.md)
  The array of title variants.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpalerttemplate/actions)*