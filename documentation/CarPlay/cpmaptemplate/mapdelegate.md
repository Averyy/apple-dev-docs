# mapDelegate

**Framework**: CarPlay  
**Kind**: property  
**Role**: Instance Property

The object that serves as the delegate of the map template.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
weak var mapDelegate: (any CPMapTemplateDelegate)? { get set }
```

```objc
@property (nonatomic, weak, nullable) id<CPMapTemplateDelegate> mapDelegate;
```

## See Also

### Handling Map Template Events
- [protocol CPMapTemplateDelegate](../cpmaptemplatedelegate.md)
  The protocol an object implements to handle events from a map template.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpmaptemplate/mapdelegate)*